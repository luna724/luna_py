import re

def extract(pattern, str, boolean=False):

    # 正規表現によるマッチング
    match = re.search(pattern, str)
    if match:
        if boolean:
            return True
        else:
            return match.group(1)  # マッチした部分を取得して返す
    else:
        if boolean:
            return False
        else:
            return None  # マッチしなかった場合はNoneを返す