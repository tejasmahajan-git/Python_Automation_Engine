import logging
import os

def setup_log():
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("system")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # File handler
        file_handler = logging.FileHandler("logs/system.log", encoding="utf-8")
        file_handler.setFormatter(formatter)

        # Console handler (optional but very useful)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        logger.propagate = False

    return logger