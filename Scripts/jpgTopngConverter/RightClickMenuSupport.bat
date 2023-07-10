@echo off

rem 管理者権限検知
NET SESSION >nul 2>&1
IF %ERRORLEVEL% EQU 0 (
    echo Loading..
) ELSE (
    echo Need Administrator
    pause
	exit
)


rem ファイルパス取得
set "current_dir=%~dp0"
set "main_dir=%current_dir%main.py"

REM レジストリキーの作成・変更
reg add HKEY_CLASSES_ROOT\.jpg\Shell\ConvertToPNG /ve /d "Convert to PNG" /f
reg add HKEY_CLASSES_ROOT\.jpg\Shell\ConvertToPNG\Command /ve /d "python "%main_dir%"" /f

echo Setup Successful
pause
exit