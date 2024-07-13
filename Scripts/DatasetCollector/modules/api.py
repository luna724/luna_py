from bs4 import BeautifulSoup
from typing import *

import requests

BASE_TEXT = "https://storage.sekai.best/sekai-jp-assets/sound/scenario/voice/event_01_01_rip/voice_ev_band_01_1_02_02.mp3"


def parse_event_link(url:List[str] | str, include_shuffle: Literal["Yes", "No"] | bool = False) -> List[str]:
  """
  URL のリストを受け取り、処理後のパターン化されたURLリストを返す
  URLリストの Syntax:
  
  https://sekai.best/storyreader/eventStory/1
  https://sekai.best/storyreader/eventStory/24
  eventStory/4
  eventStory/21
  ..
  
  include_shuffle: ユニットイベントで、対象ユニット以外のキャラクターのパターンも生成するかどうか
  False, "No" の場合は行わない
  (例: Leo/Need のイベントの場合、voice_ev_band_{}.. とし、Leo/Need のキャラクター以外の音声の取得を行わない)
  
  True, "Yes" の場合は行う、この場合大きな時間がかかる
  
  -> List[str@URLTypes]
  """
  if isinstance(url, str):
    url = [url]
  urls = url
  
  for i, url in enumerate(urls):
    if not url.startswith("https://"):
      url = f"https://sekai.best/storyreader/{url}"
    elif not url.startswith("https://sekai.best"):
      continue
    
    respond = requests.get(url)
    status = respond.status_code
    
    if not status == 200:
      print(f"Err: in parsing URL (index: {i})\nStatus Code: {status}")