#load.py
# Load function
#Imports
import logging
import os

#Logger object
logger = logging.getLogger("system")

#Defining the function
def load_data(config):
    logger.info("[LOAD] Started")

    path = config["files"]["input"] #Path from config.json

    if not os.path.exists(path):
        logger.error(f"[LOAD] Input file not found: {path}")
        raise FileNotFoundError(path)

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        data = f.readlines()
        

    if not data:
        logger.warning("[LOAD] File is empty")

    logger.info("[LOAD] Completed")

    return data

   
