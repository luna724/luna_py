@echo off
cd ..\..\..\
call .venv/Scripts/Activate
cd ./Scripts/sd_tool/prompt_EasyMaker

cd /d ./v3

python launch.py --local --ui_ip 0.0.0.0

pause