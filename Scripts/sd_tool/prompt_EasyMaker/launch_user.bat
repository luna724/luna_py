@echo off
cd ..\..\..\
call .venv/Scripts/Activate
cd ./Scripts/sd_tool/prompt_EasyMaker

cd /d ./v3

rem 現愛 v1 のみ対応
python launch.py --version v1

pause