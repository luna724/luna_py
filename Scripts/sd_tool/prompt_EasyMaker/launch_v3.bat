@echo off
cd ..\..\..\
call .venv/Scripts/Activate
cd ./Scripts/sd_tool/prompt_EasyMaker

cd /d ./v3

python launch.py --local --ui_port 7862 --new_ui

pause