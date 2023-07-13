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
set "main_dir=%windir%System32\cmd.exe %current_dir%run.bat"

REM レジストリキーの作成・変更
reg add HKEY_CLASSES_ROOT\.jpg\shell\ConvertToPNG /ve /d "Convert to PNG" /f
reg add HKEY_CLASSES_ROOT\.jpg\shell\ConvertToPNG\Command /ve /d ""%main_dir%"" /f

reg add HKEY_CLASSES_ROOT\.jpeg\shell\ConvertToPNG /ve /d "Convert to PNG" /f
reg add HKEY_CLASSES_ROOT\.jpeg\shell\ConvertToPNG\Command /ve /d ""%main_dir%"" /f

reg add HKEY_CLASSES_ROOT\.webp\shell\ConvertToPNG /ve /d "Convert to PNG" /f
reg add HKEY_CLASSES_ROOT\.webp\shell\ConvertToPNG\Command /ve /d ""%main_dir%"" /f

echo Setup Successful
pause
exit