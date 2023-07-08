@echo off
rem 管理者権限検知
NET SESSION >nul 2>&1
IF %ERRORLEVEL% EQU 0 (
	echo Processing...
	rem メインpy起動
	pip3 install psutil
	rem pip3 install subprocess
	./Script/simple.bat
) ELSE (
	python ./Script/need_admin.py
)
