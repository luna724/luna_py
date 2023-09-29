@echo off

if exist venv (
  goto :vaf
) else (
  python -m venv .venv
)

:vaf
call .venv\Scripts\activate

rem rvc Dependies Install
cd ./rvc
pip install -r requirements.txt

