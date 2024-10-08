@echo off
cd ..\..\
call .venv/Scripts/Activate
cd ./Scripts/auto_chrome

rem if --url is auto 
rem automatically detect url from mode
rem if your windows is 32bit, add argument --is32bit
python launch.py --mode tokyo_shoseki --url auto
pause