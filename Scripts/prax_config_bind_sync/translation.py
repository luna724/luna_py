lang_en = {
  "main_tab.py": [
    "Target Config path", "Browse File"
  ]
}

lang_ja = {
  "main_tab.py": [
    "対象cfgの位置", "ファイルを参照",
    "元cfgの位置", "ファイルを参照",
    "bindを置き換え (元cfgのbindが未設定の場合)",
    "安定版", "bindを変換", "簡易ロードモード",
    "すべて変換するモジュールの指定", "config 更新機",
    "変換対象モジュール", "Visualsタブのすべてを自動選択",
    "変換", "対象cfgが発見できませんでした。",
    "ファイルが選択されていません", "対象cfgは Praxのcfg ではない、または非対応バージョンです。 (対応 Prax Version v1.0.2 ~ 1.0.6)",
    ""
  ]
}

import os
def check_lang():
  if os.name != "nt":
    return lang_en
  
  else:
    # 言語✅
    return lang_ja



lang = check_lang()