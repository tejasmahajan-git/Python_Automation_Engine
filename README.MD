# Python Automation Engine

A text processing engine built in Python. Supports CLI usage, a file watcher that auto-processes 
on drop, and a Streamlit UI — all driven from a single config file.

---

## How it works

Everything runs through one pipeline:
input → process → output

That pipeline can be triggered a few different ways — you can run it manually from the CLI, 
drop a file into a folder and have it process automatically, or use the Streamlit UI if you 
prefer something visual.

---

## Quick start

```bash
pip install -r requirements.txt

# Run once
python -m system.cli run

# Watch mode (auto-processes files dropped into input_files/)
python -m system.cli watch

# UI
streamlit run app.py
```

Output lands in `output_files/`.

---

## Configuration

All processing behavior lives in `config/config.json`. No touching the source code.

```json
"process": {
  "uppercase": true,
  "reverse": false,
  "remove_empty": true
}
```

---

## Project structure
system/
├── cli.py
├── engine.py
├── pipeline.py
├── steps/
├── utils/
└── runtime/

---

## What's missing / what's next

- CSV and log file support
- Batch processing
- More granular UI controls

---

Built by Tejas Mahajan
