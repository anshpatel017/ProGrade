# ProGrade - Quick Start Guide

## 🚀 Getting Started in 5 Minutes

### Step 1: Install Dependencies
```bash
cd d:\prograde
pip install -r requirements.txt
```

### Step 2: Start the Application
```bash
python main_app.py
```

You should see:
```
 * Running on http://0.0.0.0:5000
 * Debug mode: on
```

### Step 3: Open in Browser
Navigate to: **http://localhost:5000**

---

## 📋 Features Overview

### 🔍 Repository Analyzer
**What it does**: Analyzes GitHub repositories and local projects

**How to use**:
1. Click "Repo Analyzer" in the navigation
2. Enter a GitHub URL: `https://github.com/user/repo`
   - OR a local path: `C:\path\to\project`
3. Click "Analyze Repository"
4. View results:
   - Tech stack (languages, frameworks, databases)
   - Quality metrics and scores
   - Top contributors
   - Domain classification

**Example URLs**:
- `https://github.com/torvalds/linux`
- `https://github.com/facebook/react`
- `https://github.com/python/cpython`

---

### 🖼️ Image Quality Rater
**What it does**: AI-powered image quality assessment

**How to use**:
1. Click "Image Rater" in the navigation
2. Upload an image (PNG, JPG, JPEG, GIF)
   - Drag and drop or click to browse
3. Click "Rate Image"
4. View results:
   - Quality rating (0-5 stars)
   - Confidence percentage
   - Image preview

**Supported formats**: PNG, JPG, JPEG, GIF (Max 50MB)

---

## 🎨 UI Features

### Dashboard
- Overview of both tools
- Feature descriptions
- Quick access buttons
- How-it-works guide

### Modern Design Elements
- **Gradient backgrounds**: Smooth indigo-to-purple gradients
- **Responsive layout**: Works on desktop, tablet, mobile
- **Smooth animations**: Hover effects and transitions
- **Icon integration**: Font Awesome icons throughout
- **Card-based layout**: Organized information display
- **Loading indicators**: Visual feedback during processing
- **Error handling**: Clear error messages

---

## 📁 Project Structure

```
prograde/
├── main_app.py                 # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # Full documentation
├── QUICKSTART.md              # This file
├── templates/
│   ├── index.html             # Dashboard
│   ├── repo_analyzer.html     # Repository analyzer
│   └── image_rater.html       # Image rater
├── static/
│   └── style.css              # Modern CSS styling
├── uploads/                    # Uploaded images
├── Final_Working_Model/        # Repository analysis module
└── image/                      # Image rating module
```

---

## 🔧 Troubleshooting

### Issue: "Port 5000 already in use"
**Solution**: Change the port in `main_app.py` (last line):
```python
app.run(host='0.0.0.0', port=5001, debug=True)  # Use 5001 instead
```

### Issue: "Model not loaded" error
**Solution**: Ensure these files exist:
- `Final_Working_Model/prograde_model.joblib`
- `image/best.pt`

### Issue: "No module named 'flask'"
**Solution**: Run the installation again:
```bash
pip install -r requirements.txt
```

### Issue: Repository analysis is slow
**Solution**: Large repositories take time. Be patient or try smaller repos first.

---

## 🌐 API Endpoints

### Analyze Repository
```bash
curl -X POST http://localhost:5000/api/analyze-repo \
  -H "Content-Type: application/json" \
  -d '{"repo": "https://github.com/user/repo"}'
```

### Rate Image
```bash
curl -X POST http://localhost:5000/api/rate-image \
  -F "file=@image.jpg"
```

---

## 💡 Tips & Tricks

1. **For GitHub URLs**: Use the HTTPS clone URL format
2. **For Local Paths**: Use absolute paths (e.g., `C:\Users\Name\project`)
3. **For Large Repos**: The first analysis may take 1-2 minutes
4. **For Images**: Optimize file size for faster processing
5. **Multiple Analyses**: You can analyze multiple repos/images in succession

---

## 📞 Support

For detailed documentation, see `README.md`

For module-specific help:
- Repository Analyzer: `Final_Working_Model/README.md`
- Image Rater: `image/README.md`

---

## ✨ What's Next?

- Explore different repositories
- Test with various image types
- Check the results dashboard
- Try the API endpoints
- Customize the UI (edit `static/style.css`)

**Enjoy using ProGrade! 🎉**
