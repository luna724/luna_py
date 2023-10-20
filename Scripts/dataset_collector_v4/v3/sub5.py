import new_main as main

# 変数 (コピー用)
process_id = "5"

# jsonからデータの取得
date = main.jsoncfg.read("./data.json")

url_list = date[f"list_{process_id}"]
save_dir = date["SAVE_DIRECTORY"]
cooldown = date["COOLDOWN"]

# 開始
success_count = 0
failed_count = 0
run_count = 0
total_count = len(url_list)

for url in url_list:
  data = main.save_data(url, save_dir, cooldown)

  if data:
    success_count += 1
  else:
    failed_count += 1
  run_count += 1

  # Process Running (1 / 200) [S:0 / F:1]
  print(f" Process Running ({run_count} / {total_count}) [S:{success_count} / F:{failed_count}]")
  
# 終わったら
# 既存のデータを読み込む
with open("./data.json", "r") as f:
    existing_data = main.json.load(f)

# ステータスを変更
existing_data[f"list_{process_id}_STATUS"] = True

# ファイルに新しいデータを書き込む
with open("./data.json", "w") as f:
    main.json.dump(existing_data, f)