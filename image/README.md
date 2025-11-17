# Image Rating Frontend

This adds a minimal Flask frontend so you can upload a local image and get a rating from your existing model.

Files added:

- `app.py` — Flask app that serves the upload page and calls `rate.rate_image`.
- `templates/index.html` — Simple upload form and result display.
- `static/styles.css` — Basic styles.
- `requirements.txt` — Minimal dependency list.

How to run (Windows PowerShell):

```powershell
python -m pip install -r requirements.txt
python app.py
# then open http://127.0.0.1:5000 in your browser
```

Notes:
- Keep `best.pt` and `rate.py` in the same folder as `app.py` (already the case in this workspace).
- The model is loaded once at import time by `rate.py`.
