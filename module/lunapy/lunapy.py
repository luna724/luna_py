class lunapyDefault:
  """Identifier class\nDo not initialize"""
  
  from abc import abstractmethod
  @abstractmethod
  def __init__(self):
    raise RuntimeError("This class is Identifier!")