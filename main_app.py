from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import sys
import tempfile
import shutil
import subprocess
from pathlib import Path

# Get the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FINAL_MODEL_DIR = os.path.join(BASE_DIR, 'Final_Working_Model')
IMAGE_DIR = os.path.join(BASE_DIR, 'image')

# Import Final_Working_Model components
sys.path.insert(0, FINAL_MODEL_DIR)
os.chdir(FINAL_MODEL_DIR)
import importlib.util
spec = importlib.util.spec_from_file_location("final_model_app", os.path.join(FINAL_MODEL_DIR, "app.py"))
final_model_app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(final_model_app)
analyze_repo = final_model_app.analyze
PROGRADE_MODEL_OBJ = final_model_app.PROGRADE_MODEL_OBJ

# Import Image module components
os.chdir(IMAGE_DIR)
sys.path.insert(0, IMAGE_DIR)
spec = importlib.util.spec_from_file_location("image_rate", os.path.join(IMAGE_DIR, "rate.py"))
image_rate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(image_rate)
rate_image = image_rate.rate_image

# Change back to main directory
os.chdir(BASE_DIR)

app = Flask(__name__, template_folder='templates', static_folder='static')

# Configure upload folder for images
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')


@app.route('/repo-analyzer')
def repo_analyzer():
    """Repository analyzer page"""
    return render_template('repo_analyzer.html')


@app.route('/image-rater')
def image_rater():
    """Image rater page"""
    return render_template('image_rater.html')


# ============ API Routes for Repo Analyzer ============

@app.route('/api/analyze-repo', methods=['POST'])
def api_analyze_repo():
    """Analyze a GitHub repository or local path"""
    data = request.get_json() or {}
    repo = data.get('repo', '').strip()
    
    if not repo:
        return jsonify({'error': 'Please provide a GitHub repo URL or local path'}), 400
    
    if PROGRADE_MODEL_OBJ is None:
        return jsonify({'error': 'ProGrade model not loaded. Please ensure prograde_model.joblib exists.'}), 500
    
    try:
        results = analyze_repo(repo)
        return jsonify({
            'success': True,
            'data': results
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ============ API Routes for Image Rater ============

@app.route('/api/rate-image', methods=['POST'])
def api_rate_image():
    """Rate an uploaded image"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Unsupported file type. Allowed: png, jpg, jpeg, gif'}), 400
    
    try:
        from werkzeug.utils import secure_filename
        filename = secure_filename(file.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        
        rating, confidence = rate_image(save_path)
        
        return jsonify({
            'success': True,
            'filename': filename,
            'rating': rating,
            'confidence': float(confidence),
            'image_url': f'/uploads/{filename}'
        })
    except Exception as e:
        return jsonify({'error': f'Error processing image: {str(e)}'}), 500


@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    """Serve uploaded images"""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
