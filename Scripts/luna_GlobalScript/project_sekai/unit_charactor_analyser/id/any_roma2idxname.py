def returnmode_03d(members):
    member_name = "NA"
    member_id = "NA"
    if members == "ichika" or members == "itika":
        member_name = "星乃一歌"
        member_id = "001"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "saki":
        member_name = "天馬咲希"
        member_id = "002"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "honami":
        member_name = "望月穂波"
        member_id = "003"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "shiho" or members == "siho":
        member_name = "日野森志歩"
        member_id = "004"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "kanade":
        member_name = "宵崎奏"
        member_id = "017"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "mafuyu":
        member_name = "朝比奈まふゆ"
        member_id = "018"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "ena":
        member_name = "東雲絵名"
        member_id = "019"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "mizuki":
        member_name = "暁山瑞希"
        member_id = "020"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "nene":
        member_name = "草薙寧々"
        member_id = "015"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "minori":
        member_name = "花里みのり"
        member_id = "005"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "haruka":
        member_name = "桐谷遥"
        member_id = "006"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "airi":
        member_name = "桃井愛莉"
        member_id = "007"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "shizuku" or members == "sizuku":
        member_name = "日野森雫"
        member_id = "008"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "kohane":
        member_name = "小豆沢こはね"
        member_id = "009"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "ann" or members == "an":
        member_name = "白石杏"
        member_id = "010"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "emu":
        member_name = "鳳えむ"
        member_id = "014"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "tukasa" or members == "tsukasa":
        member_name = "天馬司"
        member_id = "013"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="rui":
        member_name = "神代類"
        member_id = "016"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="tooya" or members == "touya":
        member_name = "青柳冬弥"
        member_id = "012"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="akito":
        member_name = "東雲彰人"
        member_id = "008"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="miku":
        member_name = "初音ミク"
        member_id = "021"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="rinn" or members == "rin":
        member_name = "鏡音リン"
        member_id = "022"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="renn" or members == "ren":
        member_name = "鏡音レン"
        member_id = "023"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="ruka":
        member_name = "巡音ルカ"
        member_id = "024"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="meiko" or members == "MEIKO":
        member_name = "MEIKO"
        member_id = "025"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="kaito" or members == "KAITO":
        member_name = "KAITO"
        member_id = "026"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="ALL":
        member_name = "取得機能未実装"
        member_id = "021"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    else:
        print("そのキャラクターは存在しない、または入力方法が間違っています")
        exit("Error Code 404-2 \nCharactor Not Found")
        
    return member_name, member_id