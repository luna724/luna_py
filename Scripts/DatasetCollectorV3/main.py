import requests
import time
import os
import luna_GlobalScript.project_sekai.unit_charactor_analyser.event_id.leo_need as luna
import luna_GlobalScript.project_sekai.unit_charactor_analyser.id.leo_need as luna2
import luna_GlobalScript.misc.output_folder as luna3

save_folder = luna3.output(False)
num = 0
# 入力を受け取る
x = str(input("Event ID: "))
ans_url = luna.check(x)

base_url = ans_url
save = []
success_urls = []

j = 1
l = 1
patterns = [(j, l, m, n) for j in range(1, 9) for l in range(1, 9) for m in range(1, 141) for n in range(1, 5)]

while l <= 8:
    m = 1
    n = 1
    while m <= 140:
        while n <= 4:
            url = base_url.format(j, l, m, n)
            print('Trying to get Response..')
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Success: {url}")
                success_urls.append(url)
                save.append(response)
            else:
                print(f"Failed: {url}")
            time.sleep(0.01)
            n += 1
        m += 1
        n = 1
    j += 1
    l += 1

# 成功したURLをファイルに保存する
with open("success_urls_X.txt", "w") as file:
    file.write("\n".join(success_urls))

print(f"Success URLs saved to success_urls.txt")

for z in success_urls:
    y = requests.get(z)
    num += 1
    checker = ""
    check = "_{checker}.mp3"
    returns = luna2.name_extractor(z, check)
    save_name = f"{returns}_{num}-(Event ID {x}).mp3"
    with open(os.path.join(save_folder, save_name), 'wb') as f:  # 新しく保存
        f.write(y.content)
        print('Saved to ', os.path.join(save_folder, save_name))
    time.sleep(0.01)
    print(y)