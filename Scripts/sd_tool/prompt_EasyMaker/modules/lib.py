from lunapy_module_importer import Importable
import re

class _lib:
  @staticmethod
  def re4prompt(pattern: str, text: str):
    """ コンマで区切り、対象パターンのindex0のすべてを持つリストを返す
    
    """
    prompt_piece = text.split(",")
    rtl = []
    
    for x in prompt_piece:
      x = x.strip()
      r = re.findall(pattern, x)
      if r:
        rtl.append(r[0])
    
    return rtl

  @staticmethod
  def get_value(dicts, target, rtl_if_fail="", silent=True):
    """ keyError を回避しながら辞書からの値取得を行う

    """
    if silent:
      def print(*args):
        return
    
    if not isinstance(target, str):
      return ""
    try:
      rtl = dicts[target]
    except KeyError:
      rtl = rtl_if_fail
      
      print(f"Traceback:\nKeyError: {target} in dict \n{dict}")
    return rtl

  @staticmethod
  def get_index(lists, index: int=0, rtl_if_fail="", silent=True):
    """ indexError / TypeError を回避しながらリストからの値取得を行う"""
    
    if silent:
      def print(*args):
        return
      
    if not isinstance(index, int):
      return rtl_if_fail
    
    try:
      rtl = lists[index]
    
    except IndexError:
      print(f"Traceback:\nIndexError: {index}")
      return rtl_if_fail
    
    except TypeError:
      print(f"Traceback:\nTypeError: {lists}")
      return rtl_if_fail
    
    return rtl

  @staticmethod
  def get_keys_from_dict(input_dict: dict ={}, keys_list=["", "keys"], if_fail_value=None): # 
    """This function is generated by. Colab AI
    
    KeyErrorを回避しながら辞書から複数の値の取得を行い、tuple形式で返す
    """
    return tuple(input_dict.get(key, if_fail_value) for key in keys_list)

  @staticmethod
  def get_keys_from_list(input_list: list=[], indexes_list=[0, 1], if_fail_value=None): # 
    """IndexError を回避しながらリストから複数の値の取得を行い、tuple形式で返す"""
    return tuple(_lib.get_index(input_list, key, rtl_if_fail=if_fail_value) for key in indexes_list)

class lib(Importable):
  def __init__(self):
    return
  def __call__(self, **kwargs):
    return _lib