import requests
import time

base_url = "https://storage.sekai.best/sekai-assets/sound/scenario/voice/event_01_{:02d}_rip/voice_ev_band_01_{}_{:02d}_{:02d}.mp3"

patterns = [(j, l, m, n) for j in range(1, 9) for l in range(1, 9) for m in range(1, 141) for n in range(1, 5)]

updated_patterns = []
success_urls = []

for pattern in patterns:
    url = base_url.format(pattern[0], pattern[1], pattern[2], pattern[3])
    print('Trying get Response..')
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Success: {url}")
        success_urls.append(url)
    else:
        print(f"Failed: {url}")
        if response.status_code == 404:
            updated_patterns.append(pattern)
    time.sleep(0.01)

patterns = updated_patterns

print(f"Updated Patterns Count: {len(patterns)}")

for pattern in patterns:
    url = base_url.format(pattern[0], pattern[1], pattern[2], pattern[3])
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Success: {url}")
        success_urls.append(url)
    else:
        print(f"Failed: {url}")
    time.sleep(0.01)

# 成功したURLをファイルに保存する
with open("success_urls.txt", "w") as file:
    file.write("\n".join(success_urls))

print(f"Success URLs saved to success_urls.txt")