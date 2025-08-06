import os
import uuid

from flask import Blueprint
from flask import request, jsonify
from werkzeug.utils import secure_filename

from configuration.global_configuration import UPLOAD_FOLDER
from configuration.logging_configuration import logger as log

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

upload_bp = Blueprint('upload', __name__, url_prefix='/py-fea/upload')


@upload_bp.route('', methods=['POST'])
def upload():
    log.info(f"[INCOMING REQUEST] - Upload images with request: {request}")
    if 'images' not in request.files:
        log.error("[ERROR] - No files part in the request")
        return jsonify({'error': 'No files part'}), 400

    files = request.files.getlist('images')
    saved_files = []

    for file in files:
        log.info("[INCOMING FILE] - File received: %s", file.filename)
        if file and _allowed_file(file.filename):
            # Get file extension
            ext = file.filename.rsplit('.', 1)[1].lower()
            # Generate unique filename with UUID
            unique_filename = f"{uuid.uuid4()}.{ext}"
            filepath = os.path.join(UPLOAD_FOLDER, secure_filename(unique_filename))
            file.save(filepath)
            saved_files.append(unique_filename)

    if not saved_files:
        log.error("[ERROR] - No valid image files uploaded")
        return jsonify({'error': 'No valid image files uploaded'}), 400

    log.info("[SUCCESS] - Files saved successfully: %s", saved_files)
    log.info("[SUCCESS] - Upload completed successfully")
    return jsonify({'message': 'Upload successful', 'files': saved_files}), 200


def _allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
