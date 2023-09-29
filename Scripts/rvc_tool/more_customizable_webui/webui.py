import rvc_webui.webui as rvcui
from rvc_webui.modules import cmd_opts, ui

import os
import shutil

# import LGS.misc.jsonconfig as jsoncfg

_list_dir = os.listdir

def listdir4mac(path):
    return [file for file in _list_dir(path) if not file.startswith(".")]

os.listdir = listdir4mac


def luna_code():
    # タブの表示状態を変更
    # 

    # タブを追加
    # 

    # ./tabs/lunapy_training.py -> ./rvc_webui/modules/tabs/luna_training.py
    shutil.copy("./tabs/lunapy_training.py", "./rvc_webui/modules/tabs/ltrain.py")
    
    # ./tabs/lunapy_train_function.py -> ./rvc_webui/modules/ltrain.py
    shutil.copy("./tabs/lunapy_train_function.py", "./rvc_webui/modules/ltrain.py")
    
    # ./tabs/lunapy_infering.py -> ./rvc_webui/modules/tabs/luna_infering.py
    # shutil.copy("./tabs/lunapy_infering.py", "./rvc_webui/modules/tabs/linfer.py")


# UI の定義
def webui():
  app = ui.create_ui()
  app.queue(64)
  app, local_url, share_url = app.launch(
        server_name=cmd_opts.opts.host,
        server_port=cmd_opts.opts.port,
        share=cmd_opts.opts.share,
    )

if __name__ == "__main__":
    luna_code()
    os.chdir("./rvc_webui")
    webui()