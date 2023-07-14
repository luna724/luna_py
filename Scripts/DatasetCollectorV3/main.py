import luna_GlobalScript.project_sekai.unit_charactor_analyser.id.any_roma2idxname as lunaidanalyse
import CollectMode.single_main as s
import CollectMode.multi_main as m

cd = float(input("クールダウン (0.001 =< x) (s): "))
members = input("取得したいキャラの名前(e.g: ichika)、またはユニット名を入力(e.g: Leo/need): ")
name, id = lunaidanalyse.returnmode_02d(members, True)

# リスト
run = [str(i).zfill(2) for i in range(1, 27)]
unitmode = [str(i).zfill(2) for i in range(80, 86)]
check = ["81", "82", "83", "84", "85"]

# 関数
def single_run(name, id, cd):
    print(f"Data Collecting Started... \n\
            Data Information:          \n\
            Name: {name}  |  ID: {id}  \n\
            Event ID: N/A")
    s.single(name, id, cd)

def unit_run(name, id, r1, r2):
    print(f"Data Collecting Started...          \n\
            Data Information:                   \n\
            Unit Name: {name}  | Unit ID: {id}  \n\
            Charactor ID Range: {r1} to {r2}    \n\
            Event ID: N/A")
    if id in check:
        print("マルチ取得は現在 Leo/need (ID:80) のみサポートしています。")
        exit()
    m.multi(r1, r2)

if not cd >= 0.001:
    cd = 0.01
    print(f"クールダウンはある程度の値ある必要があるので、{cd}に設定されました。")

if id in run:
    single_run(name, id, cd)

elif id in unitmode:
    if id == "80":
        range1 = 1
        range2 = 4
    elif id == "81":
        range1 = 5
        range2 = 8
    elif id == "82":
        range1 = 13
        range2 = 16
    elif id == "83":
        range1 = 9
        range2 = 12
    elif id == "84":
        range1 = 17
        range2 = 20
    elif id == "85":
        range1 = 21
        range2 = 26
    unit_run[id](name, id, range1, range2)
    