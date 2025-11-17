# ProGrade - Unified Analysis Platform

A comprehensive web application that integrates two powerful analysis tools:
1. **Repository Analyzer** - Analyze GitHub repositories and local projects
2. **Image Quality Rater** - AI-powered image quality assessment

## Features

### Repository Analyzer
- Analyze GitHub repositories or local project paths
- Detect technology stack (languages, frameworks, databases)
- Classify project domains
- Calculate quality metrics and scores
- Identify top contributors
- Support for both public URLs and local paths

### Image Quality Rater
- Upload images for AI-powered quality assessment
- Get quality ratings (0-5 scale)
- Confidence scores for predictions
- Support for PNG, JPG, JPEG, GIF formats
- Real-time image preview

## Project Structure

```
prograde/
├── main_app.py                 # Main Flask application
├── requirements.txt            # Python dependencies
├── templates/
│   ├── index.html             # Dashboard/home page
│   ├── repo_analyzer.html     # Repository analyzer page
│   └── image_rater.html       # Image rater page
├── static/
│   └── style.css              # Modern CSS styling
├── uploads/                    # Uploaded images directory
├── Final_Working_Model/        # Repository analysis module
│   ├── app.py
│   ├── prograde_core.py
│   ├── requirements.txt
│   └── [model files]
└── image/                      # Image rating module
    ├── app.py
    ├── rate.py
    ├── requirements.txt
    └── [model files]
```

## Installation

### 1. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- GitPython (Git operations)
- joblib (model serialization)
- pandas (data processing)
- scikit-learn (ML utilities)
- werkzeug (WSGI utilities)
- ultralytics (YOLO models)

### 2. Verify Model Files

Ensure the following model files exist:

**For Repository Analyzer** (`Final_Working_Model/`):
- `prograde_model.joblib` - Main analysis model
- `tech_stack_classifier.joblib` - Tech stack detection
- `tech_domain_classifier.joblib` - Domain classification
- `quality_model.joblib` - Quality scoring
- `mlb.joblib` - Multi-label binarizer
- `domain_labels.joblib` - Domain labels
- `scored_dataset.csv` - Training dataset

**For Image Rater** (`image/`):
- `best.pt` - YOLO model for image quality assessment

## Running the Application

### Start the Main Application

```bash
python main_app.py
```

The application will start on `http://0.0.0.0:5000`

Access it in your browser at:
- **Dashboard**: http://localhost:5000/
- **Repository Analyzer**: http://localhost:5000/repo-analyzer
- **Image Rater**: http://localhost:5000/image-rater

### Development Mode

The application runs in debug mode by default, which enables:
- Auto-reloading on code changes
- Detailed error messages
- Interactive debugger

## API Endpoints

### Repository Analysis

**Endpoint**: `POST /api/analyze-repo`

**Request**:
```json
{
  "repo": "https://github.com/user/repo"
}
```

**Response**:
```json
{
  "success": true,
  "data": {
    "repo_input": "https://github.com/user/repo",
    "repo_name": "repo",
    "model_report": {
      "repo_name": "repo",
      "domains": ["web", "backend"],
      "scores": {...},
      "tech_stack": {...},
      "contributors": [...]
    }
  }
}
```

### Image Rating

**Endpoint**: `POST /api/rate-image`

**Request**: Multipart form data with file upload

**Response**:
```json
{
  "success": true,
  "filename": "image.jpg",
  "rating": 4.5,
  "confidence": 0.92,
  "image_url": "/uploads/image.jpg"
}
```

## Usage Examples

### Analyzing a Repository

1. Navigate to http://localhost:5000/repo-analyzer
2. Enter a GitHub URL (e.g., `https://github.com/torvalds/linux`)
3. Or enter a local path (e.g., `C:\path\to\project`)
4. Click "Analyze Repository"
5. View detailed results including:
   - Tech stack breakdown
   - Quality metrics
   - Top contributors
   - Domain classification

### Rating an Image

1. Navigate to http://localhost:5000/image-rater
2. Upload an image (PNG, JPG, JPEG, GIF)
3. Click "Rate Image"
4. View results:
   - Quality rating (0-5)
   - Confidence percentage
   - Image preview

## UI Features

### Modern Design
- Responsive layout (desktop, tablet, mobile)
- Gradient backgrounds and smooth transitions
- Icon-based navigation
- Clean card-based layout

### Interactive Elements
- Drag-and-drop file upload
- Real-time form validation
- Loading spinners for long operations
- Error messages with helpful feedback
- Progress indicators

### Accessibility
- Semantic HTML structure
- ARIA labels for screen readers
- Keyboard navigation support
- High contrast colors

## Troubleshooting

### Model Not Loaded Error
**Error**: "ProGrade model not loaded"
- Ensure `prograde_model.joblib` exists in `Final_Working_Model/`
- Check file permissions
- Verify model file is not corrupted

### Image Upload Failed
**Error**: "Unsupported file type"
- Only PNG, JPG, JPEG, GIF are supported
- Check file size (max 50MB)
- Verify file is a valid image

### Repository Analysis Timeout
**Error**: "Analysis failed"
- Large repositories may take time
- Check internet connection for remote repos
- Verify local path exists and is readable

## Performance Tips

1. **For Large Repositories**: Use `--depth=1` for shallow clones
2. **For Image Processing**: Optimize image size before upload
3. **For Multiple Analyses**: Consider running in production mode with a WSGI server

## Production Deployment

For production use, replace the development server:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 main_app:app
```

## Technologies Used

- **Backend**: Flask, Python
- **Frontend**: HTML5, CSS3, JavaScript
- **ML/AI**: scikit-learn, YOLO, joblib
- **Version Control**: GitPython
- **Styling**: Modern CSS with gradients and animations

## License

This project is part of the ProGrade suite.

## Support

For issues or questions, please refer to the individual module documentation:
- Repository Analyzer: `Final_Working_Model/README.md`
- Image Rater: `image/README.md`
