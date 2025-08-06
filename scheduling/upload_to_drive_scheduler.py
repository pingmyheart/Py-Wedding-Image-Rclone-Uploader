import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

from configuration import environment_configuration_bean
from configuration.global_configuration import UPLOAD_FOLDER
from configuration.logging_configuration import logger as log


def schedule():
    log.info("Started scheduled task to upload files to Google Drive")
    # Create a thread pool to handle multiple uploads concurrently
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(_copy_to_drive, os.path.join(UPLOAD_FOLDER, filename))
                   for filename in os.listdir(UPLOAD_FOLDER)]

    return [future.result() for future in as_completed(futures)]


def _copy_to_drive(filepath):
    result = subprocess.run(
        ['rclone', 'copy', filepath, environment_configuration_bean.get("DRIVE_UPLOAD_REMOTE_AND_FOLDER")],
        capture_output=True,
        text=True)
    # Access stdout and stderr
    log.debug("STDOUT:")
    log.debug(result.stdout)

    log.debug("STDERR:")
    log.debug(result.stderr)

    if result.returncode == 0:
        log.info(f"Successfully copied {filepath} to Google Drive.")
        # Delete the file after copying
        os.remove(filepath)
        return 0
    else:
        log.error(f"Error copying {filepath} to Google Drive: {result.stderr}")
        return 1
