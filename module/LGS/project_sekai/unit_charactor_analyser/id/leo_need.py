def name_extractor_DatasetCollector(input, base):
    checker = "00"
    base = f"_{checker}.mp3"
    if input.count("_01.mp3") >= 1:
        return "星乃一歌"
    elif input.count("_02.mp3") >= 1:
        return "天馬咲希"
    elif input.count("_04.mp3") >= 1:
        return "日野森志歩"
    elif input.count("_03.mp3") >= 1:
        return "望月穂波"