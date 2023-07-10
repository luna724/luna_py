import os
import subprocess
import psutil
import time
x = True

def get_background_processes():
    background_processes = []
    for process in psutil.process_iter(['pid', 'name']):
        if process.status() == psutil.STATUS_IDLE:
            background_processes.append((process.info['pid'], process.info['name']))
    return background_processes

#def kill_task(process_name):
#    subprocess.call(['taskkill', '/F', '/IM', process_name])

# 使用例
while x == True:
    background_processes = get_background_processes()
    for pid, name in background_processes:
        print(f"取得: (PID: {pid}, 実行ファイル名: {name})")
    # if name == "MsMpEng.exe"
   
time.sleep(10)