@echo off
echo Setting up Python Automation Engine...

pip install -r requirements.txt

echo Running system...
python -m system.cli run

pause