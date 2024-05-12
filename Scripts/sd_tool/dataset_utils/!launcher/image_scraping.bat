@echo off
cd ..\

call ..\..\..\./.venv/scripts/activate
python launch.py --webui -m image_scraping
pause