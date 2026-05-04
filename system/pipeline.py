import time
import logging

from utils.config_loader import load_config
from utils.alert import send_alert
from utils.registry import STEP_REGISTRY
from runtime.progress import load_progress, save_progress, clear_progress

logger = logging.getLogger("system")


def run_pipeline(trigger_file=None):
    config = load_config()
    step_names = config.get("workflow", [])

    if not step_names:
        raise ValueError("Workflow is empty")

    logger.info(f"[PIPELINE] Steps: {step_names}")

    # 🧠 PROGRESS
    progress = load_progress() if trigger_file else None
    start_index = 0

    if progress:
        last_step = progress.get("last_completed_step")
        if last_step in step_names:
            start_index = step_names.index(last_step) + 1

    # 🧠 BUILD STEPS
    steps = []
    for name in step_names:
        if name not in STEP_REGISTRY:
            raise ValueError(f"Unknown step: {name}")
        steps.append(STEP_REGISTRY[name])

    # 🧠 EXECUTION
    start_time = time.time()
    logger.info("[START] Running pipeline")

    status = "SUCCESS"
    data = None

    for i in range(start_index, len(steps)):
        step = steps[i]
        step_name = step_names[i]

        logger.info(f"[STEP] {step_name}")

        attempts = 0
        retries = 2

        while attempts <= retries:
            try:
                if data is None:
                    data = step(config)
                else:
                    data = step(data, config)

                logger.info(f"[OK] {step_name}")
                save_progress(step_name)
                break

            except Exception as e:
                attempts += 1
                logger.error(f"[ERROR] {step_name} (attempt {attempts}) → {e}")

                if attempts > retries:
                    logger.error(f"[FAIL] {step_name} failed after retries")
                    send_alert(f"Pipeline failed at {step_name}", level="error")
                    return

                logger.info(f"[RETRY] Retrying {step_name}...")

    clear_progress()

    send_alert("Pipeline completed successfully")

    end_time = time.time()
    duration = round(end_time - start_time, 2)

    logger.info(f"[END] Duration: {duration}s")
    logger.info("[SUCCESS] Pipeline complete")