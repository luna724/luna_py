## this isn't a types module!
from lunapy_module_importer import Importer, Importable

""" 
modules/types.py (modules.types)
Importable形式: AnygeneratorTypes

lunapyの**Types をすべて集めたファイル
それらタイプはクラスのサブクラスとして、初期定義の省略化、アップデートの簡易化のために作られている
"""

class _generatorTypes():
  """
  生成タイプ: 生成にかかわるモジュールのコレクションを __init__ に含む
  staticmethodである関数 finalize(self, prompt, method_data=None, **kwargs) は
  finalizerを簡易的に実行するものである
  
  INDEX: 0
  """
  def __init__(self):
    self.generate_common = Importer("modules.generate.common")
    self.lib = Importer("modules.lib")
    #self.generation_finalizer = Importer("modules.generate.finalizer")
    self.config = Importer("modules.config.get")
  
  @staticmethod
  def finalizer(self, prompt, method_data:tuple | None = None, **kwargs) -> str:
    return

class generatorTypes(Importable):
  def __init__(self):
    pass
  def __call__(self, **kwargs):
    return _generatorTypes


class _collectorTypes:
  """
  取得タイプ: データの取得にかかわるモジュールを __init__ に含む
  関数 get_data_path(self) は 
  コンフィグの親パス(realpath)を返す関数である
  
  INDEX: 1
  """
  def __init__(self):
    self.config = Importer("modules.config.get")
  
  def get_data_path(self):
    return self.config.get_data_path()

class collectorTypes(Importable):
  def __init__(self):
    pass
  def __call__(self, **kwargs):
    return _collectorTypes