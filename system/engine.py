# engine.py

import logging

from utils.config_loader import load_config
from system.pipeline import run_pipeline

logger = logging.getLogger("system")


def execute(mode="manual", trigger_file=None):
    logger.info(f"[ENGINE] Mode: {mode}")

    config = load_config()

    try:
        if mode == "manual":
            run_pipeline(trigger_file=trigger_file)

        elif mode == "schedule":
            run_pipeline(trigger_file=None)

        elif mode == "event":
            run_pipeline(trigger_file=trigger_file)

        else:
            logger.error(f"[ENGINE] Unknown mode: {mode}")

    except Exception as e:
        logger.error(f"[ENGINE] Execution failed: {e}")