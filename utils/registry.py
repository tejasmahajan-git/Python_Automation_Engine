from steps.load import load_data
from steps.process import process_data
from steps.save import save_data

STEP_REGISTRY = {
    "load": load_data,
    "process": process_data,
    "save": save_data,
}