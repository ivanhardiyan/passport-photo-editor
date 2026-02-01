from flask import Flask, request, send_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'  # Ensure this folder exists
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Endpoint for photo upload
@app.route('/upload', methods=['POST'])
def upload_photo():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return 'File uploaded successfully', 200

# Endpoint for photo processing
@app.route('/process/<filename>', methods=['POST'])
def process_photo(filename):
    # Placeholder for processing logic
    # You can add your processing code here
    return 'Processed photo', 200

# Endpoint for downloading processed photo
@app.route('/download/<filename>', methods=['GET'])
def download_photo(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)