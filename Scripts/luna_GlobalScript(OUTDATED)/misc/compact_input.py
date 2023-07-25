def tfgen(inf): # tfgen (True, Falseの文字列で返す)
    if inf == "0":
        return "False"
    elif inf == "1":
        return "True"
    else:
        return str(inf)
def yngen(inf): # yngen (Yes, Noの文字列で返す)
    if inf == "0":
        return "No"
    elif inf == "1":
        return "Yes"
    else:
        return str(inf)
def tfgen_boolean(inf): # tfgen_boolean (True, Falseをboolean形式で返す)
    if inf == "0":
        return False
    elif inf == "1":
        return  True
    else:
        return str(inf)
def turnstr(inf): # turnstr (文字列にして返す)
    if inf == "0":
        return str(0)
    elif inf == "1":
        return str(1)
    else:
        return str(inf)
def isnone(inf): # isnone 何も書いていない場合、Trueを返す
    if inf == "":
        return True
    else:
        return False
def isnone_ex(inf): # 空白等を消したものを検出する
    inf = inf.split()
    inf = inf.replace("\n","")
    ret = isnone(inf)
    return ret