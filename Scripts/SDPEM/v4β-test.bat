rem echo off
call ..\..\./.venv/Scripts/Activate

python pem_launcher.py --pem-ui_ip 0.0.0.0 --testui --test_mode mt_s_lora

pause