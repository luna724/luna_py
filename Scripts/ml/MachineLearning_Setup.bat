echo If you have CUDA, please modify torch install option (PyTorch 1.13.1)

@echo off
if exist venv (
  goto :after_venv
) else (
  python -m venv .venv
)

:after_venv
call .venv\Scripts\activate
rem CPU なので CPU Torch
pip install torch==1.13.1+cpu torchvision==0.14.1+cpu torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cpu

rem CUDA があるなら (11.7)
rem pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117

rem その他
pip install -r requirements.txt
python -m pip install --upgrade pip
