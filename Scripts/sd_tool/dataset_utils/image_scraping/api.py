import argparse

def parse(
  parser:argparse.ArgumentParser
):
  def add(p:argparse.ArgumentParser, d, r, a, i, *args, **kwargs):
    if a != "":
      p.add_argument(
        i, *args, action=a, default=d, required=r
      )
    else:
      p.add_argument(
          i, *args, default=d, required=r
        )
  
  args = [ # syntax: (Default, Required, store_true, args, c)
    (None, False, "", "--image"),
    (None, False, "", "--fn"),
    ("png", False, "", "--ext"),
    (None, False, "", "--manual_cd"),
    (False, False, "store_true", "--safemode")
  ]
  for (a, b, c, d) in args:
    add(parser, a, b, c, d)