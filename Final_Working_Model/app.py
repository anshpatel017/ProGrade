from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import tempfile
import shutil
import joblib
import git
import pandas as pd
import re
import subprocess
from pathlib import Path

from prograde_core import analyze_repository

ARTIFACTS = {
    "stack_model": "tech_stack_classifier.joblib",
    "mlb": "mlb.joblib",
    "domain_model": "tech_domain_classifier.joblib",
    "domain_labels": "domain_labels.joblib",
    "quality_model": "quality_model.joblib",
    "schema_csv": "scored_dataset.csv",
}

app = Flask(__name__)

# Try to load a saved ProGrade model object at startup (used to produce the model_report)
PROGRADE_MODEL_PATH = "prograde_model.joblib"
PROGRADE_MODEL_OBJ = None
if os.path.exists(PROGRADE_MODEL_PATH):
    try:
        PROGRADE_MODEL_OBJ = joblib.load(PROGRADE_MODEL_PATH)
        # leave object as None if it doesn't have analyze
        if not hasattr(PROGRADE_MODEL_OBJ, 'analyze'):
            PROGRADE_MODEL_OBJ = None
    except Exception:
        PROGRADE_MODEL_OBJ = None


def git_commit_count(repo_path):
    try:
        out = subprocess.run([
            "git", "rev-list", "--count", "HEAD"
        ], cwd=repo_path, capture_output=True, text=True, check=True)
        return int(out.stdout.strip())
    except Exception:
        return 0


def readme_word_count(repo_path):
    try:
        for f in os.listdir(repo_path):
            if f.lower().startswith("readme"):
                with open(os.path.join(repo_path, f), "r", encoding="utf-8", errors="ignore") as fh:
                    return len(re.findall(r"\b\w+\b", fh.read()))
    except Exception:
        pass
    return 0


def extract_basic_ml_features(repo_path):
    features = {
        'num_commits': 0, 'readme_word_count': 0, 'directory_depth': 0,
        'has_test_folder': 0, 'has_eslint': 0, 'has_dockerfile': 0,
        'has_license': 0, 'has_gitignore': 0, 'has_package_json': 0,
        'has_pom_xml': 0, 'has_requirements_txt': 0,
        'count_py': 0, 'count_js': 0, 'count_md': 0, 'count_json': 0,
        'count_html': 0, 'count_css': 0, 'count_java': 0, 'count_ts': 0,
        'count_go': 0, 'count_rb': 0, 'count_php': 0,
    }
    features['num_commits'] = git_commit_count(repo_path)
    features['readme_word_count'] = readme_word_count(repo_path)
    max_depth = 0
    test_folders = {'test', 'tests', 'spec', 'specs', '__tests__'}
    for root, dirs, files in os.walk(repo_path):
        if ".git" in root.split(os.sep):
            continue
        depth = root.replace(repo_path, "").count(os.sep)
        if depth > max_depth:
            max_depth = depth
        for d in dirs:
            if d.lower() in test_folders:
                features['has_test_folder'] = 1
        for fname in files:
            lower = fname.lower()
            if lower == 'dockerfile':
                features['has_dockerfile'] = 1
            if lower.startswith('.eslintrc'):
                features['has_eslint'] = 1
            if lower.startswith('license'):
                features['has_license'] = 1
            if lower == '.gitignore':
                features['has_gitignore'] = 1
            if lower == 'package.json':
                features['has_package_json'] = 1
            if lower == 'pom.xml':
                features['has_pom_xml'] = 1
            if lower == 'requirements.txt':
                features['has_requirements_txt'] = 1
            _, ext = os.path.splitext(lower)
            if ext == '.py':
                features['count_py'] += 1
            elif ext == '.js':
                features['count_js'] += 1
            elif ext in ('.md', '.markdown'):
                features['count_md'] += 1
            elif ext == '.json':
                features['count_json'] += 1
            elif ext == '.html':
                features['count_html'] += 1
            elif ext == '.css':
                features['count_css'] += 1
            elif ext == '.java':
                features['count_java'] += 1
            elif ext == '.ts':
                features['count_ts'] += 1
            elif ext == '.go':
                features['count_go'] += 1
            elif ext == '.rb':
                features['count_rb'] += 1
            elif ext == '.php':
                features['count_php'] += 1
    features['directory_depth'] = max_depth
    return features


def align_features_to_schema(feature_dict, schema_csv_path):
    if not os.path.exists(schema_csv_path):
        return pd.DataFrame([feature_dict])
    header = pd.read_csv(schema_csv_path, nrows=0).columns.tolist()
    NON_FEATURE_COLS = ['repo_url','repo_name','tech_stack','tech_domain','quality_score']
    training_features = [c for c in header if c not in NON_FEATURE_COLS]
    df = pd.DataFrame([feature_dict])
    df_aligned = df.reindex(columns=training_features, fill_value=0)
    return df_aligned


def load_models():
    models = {}
    for k, p in ARTIFACTS.items():
        if os.path.exists(p):
            try:
                models[k] = joblib.load(p)
            except Exception:
                models[k] = None
        else:
            models[k] = None
    return models


def analyze(repo_input):
    """Only runs the saved ProGrade model's `analyze` and returns the model_report.
    If no `prograde_model.joblib` with an `analyze` method is available, raises an Exception.
    """
    if PROGRADE_MODEL_OBJ is None:
        raise RuntimeError("No prograde_model.joblib with an analyze() method is available on the server")

    is_url = repo_input.startswith("http://") or repo_input.startswith("https://") or repo_input.startswith("git@")
    tempdir = None
    repo_path = repo_input
    try:
        if is_url:
            tempdir = tempfile.mkdtemp(prefix="prograde_web_clone_")
            try:
                repo_obj = git.Repo.clone_from(repo_input, tempdir, depth=1)
                # try unshallow but ignore errors
                shallow_file = os.path.join(tempdir, ".git", "shallow")
                if os.path.exists(shallow_file):
                    try:
                        repo_obj.git.fetch("--unshallow")
                    except Exception:
                        pass
            except Exception:
                repo_obj = git.Repo.clone_from(repo_input, tempdir)
            repo_path = tempdir
        else:
            if not os.path.exists(repo_input):
                raise FileNotFoundError(f"Local path does not exist: {repo_input}")
            repo_path = os.path.abspath(repo_input)

        # Only call the saved model's analyze() and return that report
        model_report = None
        try:
            model_report = PROGRADE_MODEL_OBJ.analyze(repo_path)
        except Exception as e:
            raise RuntimeError(f"prograde_model.analyze() failed: {e}")

        combined = {
            'repo_input': repo_input,
            'repo_name': model_report.get('repo_name') if isinstance(model_report, dict) else os.path.basename(os.path.normpath(repo_path)),
            'model_report': model_report,
        }
        return combined
    finally:
        if tempdir and os.path.exists(tempdir):
            try:
                shutil.rmtree(tempdir)
            except Exception:
                pass


@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    error = None
    if request.method == 'POST':
        repo = request.form.get('repo_url', '').strip()
        if not repo:
            error = 'Please provide a GitHub repo URL or local path.'
        else:
            try:
                results = analyze(repo)
            except Exception as e:
                error = str(e)
    return render_template('index.html', results=results, error=error)


@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    data = request.get_json() or {}
    repo = data.get('repo')
    if not repo:
        return jsonify({'error': 'missing repo parameter'}), 400
    try:
        results = analyze(repo)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
