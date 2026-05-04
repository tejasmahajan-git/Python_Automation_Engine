import logging
import os

logger = logging.getLogger("system")

def save_data(data, config):
    logger.info("[SAVE] Started")

    if data is None:
        raise ValueError("No data received in save step")

    path = config["files"]["output"]
    temp_path = path + ".tmp"

    # Safe write (prevents corruption)
    with open(temp_path, "w",encoding="utf-8") as f:
        for line in data:
            f.write(line + "\n")

    os.replace(temp_path, path)

    logger.info("[SAVE] Completed")

    return data