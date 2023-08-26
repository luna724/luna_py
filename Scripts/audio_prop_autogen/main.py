import eyed3
import requests
import LGS.misc.nomore_oserror as los
from LGS.misc.re_finder import extract as re
from bs4 import BeautifulSoup
import LGS.web_tool.google as search
import os
from mutagen.flac import FLAC
from mutagen.wave import WAVE as WAV
import shutil

def load_all(TARGET_DIRECTORY):
  filelist = los.file_extension_filter(os.listdir(TARGET_DIRECTORY), [
    ".flac", ".wav", ".mp3"]) # 許可される拡張子
  filelist_MP3 = los.file_extension_filter(os.listdir(TARGET_DIRECTORY), [".mp3"])
  
  return filelist, filelist_MP3

def template_set(properties_template, inputs, TARGET_DIRECTORY):
  # 辞書から摘出
  template_title = ""
  template_artist = ""
  template_album = ""
  template_genre = ""
  template_composer = ""
  
  if properties_template["TITLE"]:
    template_title = properties_template["title"]
  
  if properties_template["ARTIST"]:
    template_artist = properties_template["artist"]
  
  if properties_template["ALBUM"]:
    template_album = properties_template["album"]
    
  if properties_template["GENRE"]:
    template_genre = properties_template["genre"]
  
  if properties_template["COMPOSER"]:
    template_composer = properties_template["composer"]
  
  
  for file in inputs:
    used_eyed3 = False
    if os.path.splitext(file)[1].lower() == ".flac":
      audiofile = FLAC(os.path.join(TARGET_DIRECTORY, file))
    
    elif os.path.splitext(file)[1].lower() == ".wav":
      audiofile = WAV(os.path.join(TARGET_DIRECTORY, file))
    
    elif os.path.splitext(file)[1].lower() == ".mp3":
      audiofile = eyed3.load(os.path.join(TARGET_DIRECTORY, file))
      used_eyed3 = True
    
    else:
      continue
    
    if used_eyed3:
        audiofile.tag.title = template_title
        audiofile.tag.artist = template_artist
        audiofile.tag.album = template_album
        audiofile.tag.genre = template_genre
        audiofile.tag.composer = template_composer
        audiofile.tag.save()   
        
    else:
        audiofile['title'] = template_title
        audiofile['artist'] = template_artist
        audiofile['album'] = template_album
        audiofile['genre'] = template_genre
        audiofile['composer'] = template_composer
        audiofile.save()
        
        

def main(target_dir, 
         auto_get_composer=False,
         songname_pattern="",
         pattern_type="replace", # or re
         template_title="",
         template_artist="",
         template_album="",
         template_genre="",
         template_composer="",
         name2title=False):
  filelist, mp3_filelist = load_all(target_dir)
  
  # セーブ
  for file in filelist:
    os.makedirs(f"{target_dir}/backups", exist_ok=True)
    shutil.copy(os.path.join(target_dir, file), os.path.join(f"{target_dir}/backups", file))
  
  # テンプレ適用
  template_dict = {
    "TITLE": False,
    "ARTIST": False,
    "ALBUM": False,
    "GENRE": False,
    "COMPOSER": False
  }
  
  if not template_title == "":
    template_dict["TITLE"] = True
    template_dict["title"] = template_title
  
  if not template_artist == "":
    template_dict["ARTIST"] = True
    template_dict["artist"] = template_artist
  
  if not template_album == "":
    template_dict["ALBUM"] = True
    template_dict["album"] = template_album
  
  if not template_genre == "":
    template_dict["GENRE"] = True
    template_dict["genre"] = template_genre
  
  if not template_composer == "":
    template_dict["COMPOSER"] = True
    template_dict["composer"] = template_composer
  
  
  # テンプレ適用
  template_set(template_dict, filelist, target_dir)
  
  # 作曲者名の自動取得
  if auto_get_composer:
    for file in filelist:
      
      if not songname_pattern == "":
        if pattern_type == "re":
          filename = re(songname_pattern, file)
        elif pattern_type == "replace":
          filename = file.replace(songname_pattern, "").strip()
      else:
        filename = file
      
      result_url = search.simple_search(f"{filename} Composer utaten.com")
      
      # <dd class="newLyricWork__body">
      #                          <a href="/songWriter/17766/">
      #        ジミーサムP            </a>
      #                                    </dd>
      
      html = requests.get(result_url)
      
      soup = BeautifulSoup(html, 'html.parser')
      new_lyric_body_elements = soup.find_all(class_='newLyricWork__body')  # classが "newLyricWork__body" の要素をすべて検索


      target_element = new_lyric_body_elements[1]
      a_tag = target_element.find('a')  # <a> 要素を検索
      result = a_tag.text.strip()  # テキストを取得して空白を削除
      
      template_dict = {
        "TITLE": False,
        "ARTIST": False,
        "ALBUM": False,
        "GENRE": False,
        "COMPOSER": True,
        "composer": result}
      
      template_set(template_dict, [file], target_dir)

  if name2title:
    for file in filelist:
      
      if not songname_pattern == "":
        if pattern_type == "re":
          filename = re(songname_pattern, file)
        elif pattern_type == "replace":
          filename = file.replace(songname_pattern, "").strip()
      else:
        filename = file
      
      template_dict = {
        "TITLE": True,
        "ARTIST": False,
        "ALBUM": False,
        "GENRE": False,
        "COMPOSER": False,
        "title": filename}
      
      template_set(template_dict, [file], target_dir)