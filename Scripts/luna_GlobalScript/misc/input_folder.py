import os

def input(IsInput):
    if IsInput == True:
        return_ = input("対象フォルダの位置を指定 (例: C:\\TEMP\\Example)\nEnter save position (e.g C:\\TEMP\\Example)\n: ")
        if not os.path.exists(return_):
            os.mkdir(return_)
        return return_
    if IsInput == False:
        return_ = "./"
        if not os.path.exists(return_):
            os.mkdir(return_)
        return return_