# Configuration settings for Flask application

import os

# Upload folder
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

# Output folder
OUTPUT_FOLDER = os.path.join(os.getcwd(), 'output')

# Allowed extensions for upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Max file size in bytes
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16 MB

