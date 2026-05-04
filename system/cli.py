import sys
import logging
from system.pipeline import run_pipeline
from system.scheduler import run_scheduler
from system.event import watch_for_file
from system.engine import execute
from utils.logger_setup import setup_log

def main():
    setup_log()
    logger = logging.getLogger("system")

    if len(sys.argv) < 2:
        logger.error("Usage: python py [run | schedule | watch]")
        return

    command = sys.argv[1]

    if command == "run":
        execute(mode="manual")


    elif command == "schedule":
        run_scheduler()

    elif command == "watch":
        watch_for_file()

    else:
        logger.error(f"Unknown command: {command}")


if __name__ == "__main__":
    main()