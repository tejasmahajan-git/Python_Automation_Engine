import time
import logging
from system.pipeline import run_pipeline
from system.engine import execute


logger = logging.getLogger("system")


def run_scheduler(interval=10):
    logger.info(f"[SCHEDULER] Started (interval={interval}s)")

    next_run = time.time()

    try:
        while True:
            current_time = time.time()

            if current_time >= next_run:
                logger.info("[SCHEDULER] Running pipeline")

                

                execute(mode="schedule")
                next_run = current_time + interval

            time.sleep(1)

    except KeyboardInterrupt:
        logger.info("[SCHEDULER] Stopped by user")