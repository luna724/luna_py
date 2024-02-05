cd ..\..\..\
call .venv/Scripts/Activate
cd ./Scripts/sd_tool/prompt_EasyMaker

cd /d ./v3

python launch.py --local --ui_port 10000 --ui_ip 0.0.0.0 --open_browser

pause