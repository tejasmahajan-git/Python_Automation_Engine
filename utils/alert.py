#Importing
import logging
logger = logging.getLogger("system")
#Functions
def send_alert(message, level="info"):
    if level == "info":
        logger.info(f"[ALERT] {message}")
        print(f"[ALERT] {message}")

    elif level == "error":
        logger.error(f"[ALERT] {message}")
        print(f"[ALERT] {message}")
