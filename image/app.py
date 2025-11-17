from flask import Flask, request, render_template, send_from_directory
import os
from werkzeug.utils import secure_filename

# Import the existing rating function
from rate import rate_image

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file part in the request')
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error='No file selected')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)
            try:
                rating, confidence = rate_image(save_path)
            except Exception as e:
                return render_template('index.html', error=f'Error running model: {e}')
            return render_template('index.html', result=True, filename=filename, rating=rating, confidence=confidence)
        else:
            return render_template('index.html', error='Unsupported file type')
    return render_template('index.html')


@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
