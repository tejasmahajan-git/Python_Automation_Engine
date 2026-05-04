import logging

logger = logging.getLogger("system")

def should_run(file_path):
    try:
        with open(file_path, "r") as f:
            content = f.read()

        return "RUN" in content

    except FileNotFoundError:
        logger.error(f"[CONDITION] File not found: {file_path}")
        return False

    except Exception as e:
        logger.error(f"[CONDITION] Error reading file: {e}")
        return False