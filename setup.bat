@echo off
rem Create venv
:venv
if exist venv (
    goto :pip_ins
) else (
    python -m venv venv   
)

rem Install Requirements.txt
:pip_ins
call venv\scripts\activate
pip3 install -r requirements.txt

rem Update pip
python -m pip install --upgrade pip

rem luna_GlobalScriptの取得
if exist ./venv/Scripts/site-packages/luna_GlobalScript (
    rem 存在する場合、アップデート
    rd ./venv/Scripts/site-packages/luna_GlobalScript /q
    xcopy "./Scripts/luna_GlobalScript" "./venv/Lib/site-packages/luna_GlobalScript" /e /c /i /y
) else (
    xcopy "./Scripts/luna_GlobalScript" "./venv/Lib/site-packages/luna_GlobalScript" /e /c /i /y
)