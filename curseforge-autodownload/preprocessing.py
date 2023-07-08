import url_open as open
def preprocessing(get, mcver):
    openwith_def = []
    for pre in get:
        pre = pre[0]
        if pre.count("/comments") >= 1: # 拡張URLがついている場合、消す
            pre = pre.replace("/comments", "/")
        elif pre.count("/files") >= 1:
            pre = pre.replace("/files", "/")
        elif pre.count("/screenshots") >= 1:
            pre = pre.replace("/screenshots", "/")
        else:
            if pre.startswith("https://www.curseforge.com/minecraft/mc-mods/"):
                # minecraft/mc-mods の、Minecraft MODタイプのURLの場合、普通に / を追加
                pre = f"{pre}/"
                print(f"{pre}")
            else:
                print(f"{pre}\nThis URL was excluded because it is not a Minecraft MOD")

        # pre処理後の処理
        pre = f"{pre}files?version={mcver}"
        openwith_def.append(pre)

        # URLを開いて、ダウンロードを実行する処理
        return_ = open.open([openwith_def])
        return return_