

def print_locals(*args):
  for k, v in locals().items():
    print(k, ": ", v)
  return