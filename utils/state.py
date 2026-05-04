from datetime import datetime
import os

STATE_FILE = "runtime/last_run.txt"

def get_last_run_date():
    if not os.path.exists(STATE_FILE):
        return None

    with open(STATE_FILE, "r") as f:
        return f.read().strip()

def set_last_run_date():
    os.makedirs("runtime", exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")

    temp_path = STATE_FILE + ".tmp"

    with open(temp_path, "w") as f:
        f.write(today)

    os.replace(temp_path, STATE_FILE)