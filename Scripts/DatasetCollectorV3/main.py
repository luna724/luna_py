import luna_GlobalScript.project_sekai.unit_charactor_analyser.id.any_roma2idxname as lunaidanalyse
import CollectMode.single_main as s
import CollectMode.multi_main as m

members = input("取得したいキャラの名前(e.g: ichika)、またはユニット名を入力(e.g: Leo/need): ")
name, id = lunaidanalyse.returnmode_02d(members, True)

# リスト
run = [str(i).zfill(2) for i in range(1, 27)]
unitmode = [str(i).zfill(2) for i in range(80, 86)]
check = ["81", "82", "83", "84", "85"]

# 関数
def single_run(name, id):
    print(f"Data Collecting Started... \
            Data Information:  \
            Name: {name}  |  ID: {id}  \
            Event ID: N/A")
    s.single(name, id)

def unit_run(name, id, r1, r2):
    print(f"Data Collecting Started...  \
            Data Information:  \
            Unit Name: {name}  | Unit ID: {id}  \
            Charactor ID Range: {r1} to {r2}  \
            Event ID: N/A")
    if id in check:
        print("マルチ取得は現在 Leo/need (ID:80) のみサポートしています。")
        exit()
    m.multi(r1, r2)


if id in run:
    single_run(name, id)

elif id in unitmode:
    if id == "80":
        range1 = 1
        range2 = 4
    unit_run[id](name, id, range1, range2)
    