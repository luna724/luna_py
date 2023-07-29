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

def returnmode_02d(members, unit_mode):
    member_name = "NA"
    member_id = "NA"
    if members == "ichika" or members == "itika":
        member_name = "星乃一歌"
        member_id = "01"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "saki":
        member_name = "天馬咲希"
        member_id = "02"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "honami":
        member_name = "望月穂波"
        member_id = "03"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "shiho" or members == "siho":
        member_name = "日野森志歩"
        member_id = "04"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "kanade":
        member_name = "宵崎奏"
        member_id = "17"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "mafuyu":
        member_name = "朝比奈まふゆ"
        member_id = "18"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "ena":
        member_name = "東雲絵名"
        member_id = "19"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "mizuki":
        member_name = "暁山瑞希"
        member_id = "20"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "nene":
        member_name = "草薙寧々"
        member_id = "15"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "minori":
        member_name = "花里みのり"
        member_id = "05"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "haruka":
        member_name = "桐谷遥"
        member_id = "06"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "airi":
        member_name = "桃井愛莉"
        member_id = "07"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "shizuku" or members == "sizuku":
        member_name = "日野森雫"
        member_id = "08"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "kohane":
        member_name = "小豆沢こはね"
        member_id = "09"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "ann" or members == "an":
        member_name = "白石杏"
        member_id = "10"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "emu":
        member_name = "鳳えむ"
        member_id = "14"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members == "tukasa" or members == "tsukasa":
        member_name = "天馬司"
        member_id = "13"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="rui":
        member_name = "神代類"
        member_id = "16"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="tooya" or members == "touya":
        member_name = "青柳冬弥"
        member_id = "12"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="akito":
        member_name = "東雲彰人"
        member_id = "11"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="miku":
        member_name = "初音ミク"
        member_id = "21"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="rinn" or members == "rin":
        member_name = "鏡音リン"
        member_id = "22"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="renn" or members == "ren":
        member_name = "鏡音レン"
        member_id = "23"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="ruka":
        member_name = "巡音ルカ"
        member_id = "24"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="meiko" or members == "MEIKO":
        member_name = "MEIKO"
        member_id = "25"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="kaito" or members == "KAITO":
        member_name = "KAITO"
        member_id = "26"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif members =="ALL":
        member_name = "取得機能未実装"
        member_id = "21"
        print(f"Successfully Getting Charactor Data\nName:{member_name} ID:{member_id}")
    elif unit_mode == True:
        if members == "Leo/need" or members == "leo/need":
            member_name = "Leo/need"
            member_id = "80"
            print(f"Successfully Getting Unit Data\nName:{member_name} ID:{member_id} Member ID: 01, 02, 03, 04")
        elif members == "MORE MORE JUMP!" or members == "more more jump!":
            member_name = "MORE MORE JUMP!"
            member_id = "81"
            print(f"Successfully Getting Unit Data\nName:{member_name} ID:{member_id} Member ID: 05, 06, 07, 08")
        elif members == "Wonderlands×Showtime" or members == "ワンダーランズ×ショウタイム" or members == "ワンダショ":
            member_name = "Wonderlands×Showtime"
            member_id = "82"
            print(f"Successfully Getting Unit Data\nName:{member_name} ID:{member_id} Member ID: 13, 14, 15, 16")
        elif members == "Vivid BAD SQUAD" or members == "ビビバス":
            member_name = "Vivid BAD SQUAD"
            member_id = "83"
            print(f"Successfully Getting Unit Data\nName:{member_name} ID:{member_id} Member ID: 09, 10, 11, 12")
        elif members == "25時、ナイトコードで。" or members == "Nightcode at 25ji":
            member_name = "25時、ナイトコードで。"
            member_id = "84"
            print(f"Successfully Getting Unit Data\nName:{member_name} ID:{member_id} Member ID: 17, 18, 19, 20")
        elif members == "Virtual Singers" or members == "バーチャルシンガー" or members == "バチャシン":
            member_name = "Leo/need"
            member_id = "85"
            print(f"Successfully Getting Unit Data\nName:{member_name} ID:{member_id} Member ID: 21, 22, 23, 24, 25, 26")  
        else:
            print("そのキャラクターは存在しない、または入力方法が間違っています")
            raise {"ValueError: Can't Analyse Charactor Data"}
    else:
        print("そのキャラクターは存在しない、または入力方法が間違っています")
        exit()
        
    return member_name, member_id