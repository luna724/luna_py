def tfgen(inf): # tfgen (True, Falseの文字列で返す)
    if inf == 0:
        return "False"
    elif inf == 1:
        return "True"
    else:
        return str(inf)
def yngen(inf): # yngen (Yes, Noの文字列で返す)
    if inf == 0:
        return "No"
    elif inf == 1:
        return "Yes"
    else:
        return str(inf)
def tfgen_boolean(inf): # tfgen_boolean (True, Falseをboolean形式で返す)
    if inf == 0:
        return "False"
    elif inf == 1:
        return "True"
    else:
        return str(inf)
def turnstr(inf): # turnstr (文字列にして返す)
    if inf == 0:
        return str(0)
    elif inf == 1:
        return str(1)
    else:
        return str(inf)