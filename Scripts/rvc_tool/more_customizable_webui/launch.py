import sys
sys.path.append("./")

import rvc_webui.launch as rvc
import shlex
import os
import subprocess
import importlib.util

# キャッチしない要素の定義
commandline_args = os.environ.get("COMMANDLINE_ARGS", "")
sys.argv += shlex.split(commandline_args)

python = sys.executable
git = os.environ.get("GIT", "git")
index_url = os.environ.get("INDEX_URL", "")
stored_commit_hash = None
skip_install = False

def prepare_enviroment():
    commit = rvc.commit_hash()

    print(f"Python {sys.version}")
    print(f"Commit hash: {commit}")

    torch_command = os.environ.get(
        "TORCH_COMMAND",
        "pip install torch torchaudio --extra-index-url https://download.pytorch.org/whl/cu118",
    )

    sys.argv, skip_install = rvc.extract_arg(sys.argv, "--skip-install")
    if skip_install:
        return

    sys.argv, reinstall_torch = rvc.extract_arg(sys.argv, "--reinstall-torch")
    ngrok = False

    if reinstall_torch or not rvc.is_installed("torch") or not is_installed("torchaudio"):
        rvc.run(
            f'"{python}" -m {torch_command}',
            "Installing torch and torchaudio",
            "Couldn't install torch",
        )

#    if not rvc.is_installed("pyngrok") and ngrok:
#        rvc.run_pip("install pyngrok", "ngrok")

    rvc.run(
        f'"{python}" -m pip install -r requirements.txt',
        desc=f"Installing requirements",
        errdesc=f"Couldn't install requirements",
    )

def start():
    os.environ["PATH"] = (
        os.path.join(os.path.dirname(__file__), "bin")
        + os.pathsep
        + os.environ.get("PATH", "")
    )
    subprocess.run(
        [python, "webui.py", *sys.argv[1:]],
    )
    
# 実行
if __name__ == "__main__":
  prepare_enviroment()
  
  start()