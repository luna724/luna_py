@echo off
rem Create venv
if exist venv (
    goto :venv
) else (
    rem Venv Question
    echo Do you want use venv? (Y/N)
    choice /c YN

    if errorlevel 2 (
        echo Local Support COMING SOON.. 
        python -m venv venv
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
cd /d ./module/lgs
pip3 install -e .
cd /d ..\
pip3 install luna_GlobalScript
goto :lgs_old

:pip_ins
pip install -r requirements.txt
cd /d ./module
pip install -e .
exit

rem 今後削除予定
:lgs_old
rem luna_GlobalScriptの取得
if exist ./venv/Lib/site-packages/luna_GlobalScript (
     rem 存在する場合、アップデート
     rd ./venv/Lib/site-packages/luna_GlobalScript /q
     xcopy "./Scripts/luna_GlobalScript" "./venv/Lib/site-packages/luna_GlobalScript" /e /c /i /y
     rd ./venv/Lib/site-packages/lgs /q
     xcopy "./module/LGS" "./venv/Lib/site-packages/lgs" /eciy
) else (
     xcopy "./Scripts/luna_GlobalScript(OUTDATED)/" "./venv/Lib/site-packages/luna_GlobalScript" /e /c /i /y
     xcopy "./module/LGS" "./venv/Lib/site-packages/lgs" /eciy
)

echo Done.
pause