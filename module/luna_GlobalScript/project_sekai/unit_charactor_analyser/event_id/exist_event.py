def check_single(x, id): # イベントID 存在確認
# Unknown Error (Can't Success 100%)
# id76 = Server Error 
    # Last Update 2023/07/14 (ID: 100 仮面の私にさよならを にーご まふゆバナー)
    id_check = [str(i).zfill(2) for i in range(1, 101)]
    if x not in id_check:
        print('Invalid Event ID')
        exit()
    else:
        url_dict = {
            # Leo/need
            "1": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_01_{:02d}_rip/voice_ev_band_01_{}_{:02d}_" + f"{id}.mp3",
            "10": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_10_{:02d}_rip/voice_ev_band_02_{:02d}_{:02d}_" + f"{id}.mp3",
            "20": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_20_{:02d}_rip/voice_ev_band_03_{:02d}_{:02d}_" + f"{id}.mp3",
            "27": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_27_{:02d}_rip/voice_sc_ev_band_04_{:02d}_{:02d}_" + f"{id}.mp3",
            "13": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_13_{:02d}_rip/voice_ev_shuffle_04_{:02d}_{:02d}_" + f"{id}.mp3",
            "16": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_16_{:02d}_rip/voice_ev_shuffle_05_{:02d}_{:02d}_" + f"{id}.mp3",
            "18": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_18_{:02d}_rip/voice_ev_shuffle_06_{:02d}_{:02d}_" + f"{id}.mp3",
            "34": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_34_{:02d}_rip/voice_ev_band_05_{:02d}_{:02d}_" + f"{id}.mp3",
            "40": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_40_{:02d}_rip/voice_ev_band_06_{:02d}_{:02d}_" + f"{id}.mp3",
            "50": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_50_{:02d}_rip/voice_ev_band_07_{:02d}_{:02d}_" + f"{id}.mp3",
            "56": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_56_{:02d}_rip/voice_ev_band_08_{:02d}_{:02d}_" + f"{id}.mp3",
            "65": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_65_{:02d}_rip/voice_ev_band_09_{:02d}_{:02d}_" + f"{id}.mp3",
            "69": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_69_{:02d}_rip/voice_ev_band_10_{:02d}_{:02d}_" + f"{id}.mp3",
            "76": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_76_{:02d}_rip/voice_ev_band_11_{:02d}_{:02d}_" + f"{id}.mp3",
            "83": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_83_{:02d}_rip/voice_ev_band_12_{:02d}_{:02d}_" + f"{id}.mp3",
            "91": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_91_{:02d}_rip/voice_ev_band_13_{:02d}_{:02d}_" + f"{id}.mp3",
            "01": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_01_{:02d}_rip/voice_ev_band_01_{}_{:02d}_" + f"{id}.mp3",
            
            # Shuffle (混合)
            "30": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_30_{:02d}_rip/voice_sc_ev_shuffle_10_{:02d}_{:02d}_" + f"{id}.mp3",
            "63": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_63_{:02d}_rip/voice_ev_shuffle_21_{:02d}_{:02d}_" + f"{id}.mp3",
            "84": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_84_{:02d}_rip/voice_ev_shuffle_28_{:02d}_{:02d}_" + f"{id}.mp3",
            "90": "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_90_{:02d}_rip/voice_ev_shuffle_30_{:02d}_{:02d}_" + f"{id}.mp3"
        }
        url = url_dict.get(x)
        return url