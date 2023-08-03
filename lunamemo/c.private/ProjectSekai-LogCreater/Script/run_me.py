"""
曲の履歴やらなんやらを、スクショから取得できるもの
簡単に見返せたり、作れるので便利


座標集

曲名の取得
285 10 to 1170 63

難易度の取得 (English Only)
466 126 to 286 78

スコアの取得 (Intergler Only)
249 289 to 835 429
Challeng Live 154 288 to 732 411

ハイスコアの取得 (Intergler Only)
582 454 to 863 519
Challange Live 286 506 to 653 587

コンボ数の取得
780 852 to 331 695 (Integler Only)
Challenge Live 188 819 to 607 977

FC, AP検出 (文字版)
770 567 to 1053 620 (English Only)
Challenge Live 606 688 to 890 736

PERFECT数の取得
1007 651 to 1124 691
Challenge Live 850 768 to 962 811

GREAT数の取得
1013 696 to 1119 744
Challange Live 851 818 to 958 861

GOOD数の取得
1011 752 to 1120 798
Challenge Live 850 873 to 975 915

BAD数の取得
1013 806 to 1119 850
Challange Live 850 927 to 960 968

MISS数の取得
1009 855 to 1120 899
Challenge Live 851 977 to 957 1019

LATE数の取得
1174 749 to 1240 779
Challange Live 1011 868 to 1082 901

FAST数の取得
1381 749 to 1311 779
Challenge Live 1147 869 to 1216 898

FLICK数の取得
1319 808 to 1379 841
Challenge Live 1158 926 to 1218 962

ランクの取得 (画面上版)
1969 151 to 1866 34

Challengeか否かの取得
1308 496 to 1340 545 is "P" ?

"""
# ファイル名の重複阻止
import datetime
import LGS.misc.re_finder as ref
time = datetime.datetime.now()
time = str(time)
time = time.replace(":", "-")
time = time.replace(".", "-")
time = time.replace(" ", "-")
day_data = ref.extract(r"(\d+-\d+-\d+)\ \d+", time)


# 相対的に書き込めるように
import os
os.chdir("..\\")
root_fp = os.getcwd()
os.makedirs(f"./Logs/{time}", exist_ok=True)
os.chdir(f"./Logs/{time}")

# ファイルのリストアップ
import LGS.misc.nomore_oserror as los
filelist = []
loadlist = os.listdir(f"{root_fp}/input")
pic_loadlist = los.file_extension_filter(loadlist, allowed_extensions=["png", "jpg", "jpeg"])

# ! で開始してたら除外  
for x in pic_loadlist:
    if x.startswith("!"):
        continue
    else:
        filelist.append(x)
    
# ファイルのロード
from PIL import Image
import pytesseract as pyt
import sqlite3
def img2str(img, box, lang="digits"):
    r = pyt.image_to_string(img, boxes=box, lang=lang)
    return r

sqlite_database = []
markdown = f"""
<details> \n
<summary>{day_data}</summary>\n

"""
    
for picture in filelist:
    # 入力位置に移動
    os.chdir(f"{root_fp}/input")
    
    # ファイルの日付の取得
    ssday_data = ref.extract(r"\Screenshot_(\d+)\-\d+\.png", picture)
    sqdb = ref.extract(r"\Screenshot_\d+\-(\d+)\.png", picture)
    sqlite_database.append(sqdb)
    
    # 読み込み
    img = Image.open(picture)
    
    # 曲名を song_name に代入
    bbox = (265, 10, 1170, 63)
    song_name = pyt.image_to_string(img, boxes=bbox, lang="jpn+eng+digits")

    # チャレンジモードの取得
    cm_check = img2str(img, box=(1308, 496, 1340, 545), lang="eng")
    if cm_check == "P":
        cm = True
    else:
        cm = False
    
    if not cm:
        # スコア、ハイスコアの取得
        score = img2str(img, box=(249, 289, 835, 429))
        hscore = img2str(img, box=(582, 454, 863, 519))
        
        # コンボ数の取得
        combo = img2str(img, box=(780, 852, 331, 695))
        
        # PGGBM の取得
        perfect = img2str(img, box=(1007, 651, 1124, 691))
        great = img2str(img, box=(1013, 696, 1119, 744))
        good = img2str(img, box=(1011, 752, 1120, 798))
        bad = img2str(img, box=(1013, 806, 1119, 850))
        miss = img2str(img, box=(1009, 855, 1120, 899))

        # L/F  Flickの取得
        late = img2str(img, box=(1174, 749, 1240, 779))
        fast = img2str(img, box=(1381, 749, 1311, 779))
        flick = img2str(img, box=(1319, 808, 1379, 841))
        
        # FC, AP
        state_pyt = img2str(img, box=(770, 567, 1053, 620), lang="eng")
    
    elif cm:
        # スコア、ハイスコアの取得
        score = img2str(img, box=(154, 288, 732, 411))
        hscore = img2str(img, box=(286, 506, 653, 587))
    
        # コンボ数の取得
        combo = img2str(img, box=(188, 819, 607, 977))
        
        # PGGBM
        perfect = img2str(img, box=(850, 768, 962, 811))
        great = img2str(img, box=(851, 818, 958, 861))
        good = img2str(img, box=(850, 873, 975, 915))
        bad = img2str(img, box=(850, 927, 960, 968))
        miss = img2str(img, bo=(851, 977, 957, 1019))
        
        # L/F Flick
        late = img2str(img, box=(1011, 868, 1082, 901))
        fast = img2str(img, box=(1147, 869, 1216, 898))
        flick = img2str(img, box=(1158, 926, 1218, 962))

        # Fc, ap
        state_pyt = img2str(img, box=(606, 688, 890, 736), lang="eng")

    # スコアランク
    sr_pyt = img2str(img, box=(1969, 151, 1866, 34), lang="eng")
    
    # SQLディレクトリに移動
    os.chdir(f"{root_fp}/Logs/{time}")
    
    # SQLiteを使用して、一時的に保存
    conn = sqlite3.connect(f"{sqdb}.db")
    cursor = conn.cursor()
    
    # sqdb に応じたテーブルを作成
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {sqdb} (
                        id INTEGER PRIMARY KEY,
                        song TEXT,
                        score INTEGER,
                        hscore INTEGER,
                        combo INTEGER,
                        perfect INTEGER,
                        great INTEGER,
                        good INTEGER,
                        bad INTEGER,
                        miss INTEGER,
                        late INTEGER,
                        fast INTEGER,
                        flick INTEGER,
                        capday INTEGER
                        )""")
    
    # 代入
    cursor.execute(f"""INSERT INTO {sqdb}
                   (song, score, hscore, combo, perfect, great, good, bad, miss, late, fast, flick, capday) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                   (song_name, score, hscore, combo, perfect, great, good, bad, miss, late, fast, flick, ssday_data))
    
    # 適用、終了
    conn.commit()
    conn.close()