import os

_project_base_path = os.path.dirname(os.path.abspath(__file__))
_project_base_path = _project_base_path.replace("/configuration", "")
UPLOAD_FOLDER = f"{_project_base_path}/uploads"
