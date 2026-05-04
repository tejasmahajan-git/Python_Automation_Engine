#Imports
import logging

#Logger object
logger = logging.getLogger("system")

#Process Function
def process_data(data, config):
    logger.info("[PROCESS] Started")

    if data is None:
        raise ValueError("No data received in process step") 

    settings = config.get("process", {})
    result = []

    for line in data:
        cleaned = line.strip()

        if settings.get("uppercase"): 
            cleaned = cleaned.upper()

        if settings.get("reverse"):
            cleaned = cleaned[::-1]
        if settings.get("remove_empty"):
            if not cleaned:
                continue

        if settings.get("strip_spaces"):
            cleaned = cleaned.strip()
        result.append(cleaned)

    logger.info("[PROCESS] Completed")

    return result