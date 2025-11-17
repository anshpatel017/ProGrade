# ProGrade Web UI

This is a minimal Flask frontend for the ProGrade analysis contained in this folder. It allows you to paste a GitHub repository URL (or local path) and shows the heuristic + model outputs.

Quick start (PowerShell on Windows):

```powershell
# create a venv (optional but recommended)
python -m venv .venv;
.\.venv\Scripts\Activate.ps1;
pip install -r requirements.txt;
python app.py
```

Open http://localhost:5000 in your browser. The app will clone remote repos into a temp folder; local paths must be accessible by the server.

Notes:
- The app will attempt to use existing joblib artifacts (`prograde_model.joblib`, `quality_model.joblib`, etc.) found in this folder. If they're missing, only the heuristic `analyze_repository` will run.
- Long analysis (large repos) may take time; check console for progress.
