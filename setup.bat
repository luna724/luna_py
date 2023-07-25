@echo off
rem Create venv
if exist venv (
    goto :venv
) else (
    rem Venv Question
    echo Do you want use venv? (Y/N)
    choice /c YN

    if errorlevel 2 (
        goto :pip_ins
    ) else (
        python -m venv venv 
        goto :venv
    )
)

rem Install Requirements.txt
:venv
call venv\scripts\activate
pip3 install -r requirements.txt
python -m pip install --upgrade pip
cd /d ./module
pip3 install -e .
exit

:pip_ins
pip install -r requirements.txt
cd /d ./module
pip install -e .
exit

rem Update pip


rem LGS, Luna_GlobalScriptのインストール

rem luna_GlobalScriptの取得
rem if exist ./venv/Lib/site-packages/luna_GlobalScript (
rem     rem 存在する場合、アップデート
rem     rd ./venv/Lib/site-packages/luna_GlobalScript /q
rem     xcopy "./Scripts/luna_GlobalScript" "./venv/Lib/site-packages/luna_GlobalScript" /e /c /i /y
rem ) else (
rem     xcopy "./Scripts/luna_GlobalScript" "./venv/Lib/site-packages/luna_GlobalScript" /e /c /i /y
rem )