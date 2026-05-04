import json
import os

def load_config(path="config/config.json"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")

    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in config: {e}")