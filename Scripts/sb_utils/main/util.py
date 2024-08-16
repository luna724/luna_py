class via_ctx:
  """使用法:
  discord 以外からのBOTの呼び出し用に使用
  ctx.method() で呼び出されるものを (botが使用するもののみ)網羅しているため
  NotDefinedError を起こさない
  
  また via_ctx(func) を渡すことで
  ctx.send() 時に arg, kw を渡される関数を設定することができる
  それにて渡された関数の帰り値は self.returns に保管され
  via_ctx.get_return で取得可能
  """
  @staticmethod
  def specify_function(*a,**k):
    return None
  
  def __init__(self, send_specify_function=None):
    if not send_specify_function is None:
      self.extend = send_specify_function
    else:
      self.extend = via_ctx.specify_function
    self.returns = None
    
  async def send(self, *arg, **kw):
    self.returns = self.extend(*arg, **kw)
    return self.returns if self.returns is not None else "Message sent successfully"
  
  def get_return(self):
    return self.returns