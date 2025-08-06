import os
import signal
import sys

from flask import Flask
from flask_cors import CORS

import scheduling
from configuration.global_configuration import UPLOAD_FOLDER
from configuration.logging_configuration import logger as log
from controller import blueprints
from scheduling import scheduler
from scheduling.upload_to_drive_scheduler import schedule

app = Flask(__name__)
CORS(app)

for blueprint in blueprints:
    app.register_blueprint(blueprint)

[log.info(f"Import {_module} module") for _module in [scheduling]]

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def handle_signal(signum, frame):
    log.info(f"Received signal {signum}, shutting down...")
    scheduler.shutdown()
    schedule()
    # Perform cleanup here
    sys.exit(0)


signal.signal(signal.SIGINT, handle_signal)  # CTRL+C
signal.signal(signal.SIGTERM, handle_signal)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True, use_reloader=False)
