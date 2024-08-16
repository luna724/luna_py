
class values:
  def __init__(self):
    self.treas:dict = {
      
    }
    pass
  
  def __call__(self, key, rtl_if_fail=None):
    if hasattr(self, key):
      return getattr(self, key)
    else:
      return rtl_if_fail

value = values()