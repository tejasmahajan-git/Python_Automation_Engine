import os
import time
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from system.engine import execute

logger = logging.getLogger("system")


class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path

        logger.info(f"[EVENT] New file detected: {file_path}")

        try:
            # Update config dynamically
            import json

            with open("config/config.json", "r") as f:
                config = json.load(f)

            filename = os.path.basename(file_path)
            output_path = f"output_files/{filename}"

            config["files"]["input"] = file_path
            config["files"]["output"] = output_path

            with open("config/config.json", "w") as f:
                json.dump(config, f, indent=2)

            # Run pipeline
            execute(mode="event", trigger_file=file_path)

        except Exception as e:
            logger.error(f"[EVENT] Error: {e}")


def watch_for_file(path="input_files"):
    logger.info(f"[WATCH] Watching folder: {path}")

    os.makedirs(path, exist_ok=True)
    os.makedirs("output_files", exist_ok=True)

    event_handler = FileHandler()
    observer = Observer()

    observer.schedule(event_handler, path=path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("[WATCH] Stopped by user")
        observer.stop()

    observer.join()