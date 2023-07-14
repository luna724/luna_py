import requests
import time
import os
import luna_GlobalScript.project_sekai.unit_charactor_analyser.event_id.exist_event as check
# import luna_GlobalScript.project_sekai.unit_charactor_analyser.id.leo_need as luna2
import luna_GlobalScript.misc.output_folder as luna3

def single(name, id, cd):
    save_folder = luna3.output(False)
    # 入力を受け取る
    x = str(input("Event ID: "))
    base_url = check.check_single(x, id)

    save = []
    success_urls = []
    cds = cd * 2
    j = 1
    l = 1
    num = 0
    while l <= 8:
        m = 1
        while m <= 140:
            url = base_url.format(j, l, m)
            print('Trying to get Response..')
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Success: {url}")
                success_urls.append(url)
                save.append(response)
            else:
                  print(f"Failed: {url}")
            time.sleep(cd)
            m += 1
        j += 1
        l += 1

    # 成功したURLをファイルに保存する
    with open("success_urls_X.txt", "w") as file:
        file.write("\n".join(success_urls))

    print(f"Success URLs saved to success_urls.txt")

    for z in success_urls:
        y = requests.get(z)
        num += 1
        #checker = ""
        #check = "_{checker}.mp3"
        #returns = luna2.name_extractor_DatasetCollector(z, check)
        save_name = f"{name}_{num}-(Event ID {x}).mp3"
        with open(os.path.join(save_folder, save_name), 'wb') as f:  # 新しく保存
            f.write(y.content)
            print('Saved to ', os.path.join(save_folder, save_name))
        time.sleep(cds)
        print(f"Saved Data From {z}\nto {y}")