import numpy as np
import PIL
from PIL import Image, ImageChops, ImageDraw
import gradio as gr

#JUMP> function(visualize)


# ratios = split_ratio
# mmode = split_mode
# usecom = use common prompt
# usencom = use common negative prompt
# usebase = use base prompt
# flipper = flip , an ;
# thei = height / twid = width
# dummy_image = ?
# alpha = overlay_ratio

# Keywords
KEYROW = "ADDROW"
KEYCOL = "ADDCOL"
KEYBASE = "ADDBASE"
KEYCOMM = "ADDCOMM"
KEYBRK = "BREAK"
KEYPROMPT = "ADDP"
DELIMROW = ";"
DELIMCOL = ","
MCOLOUR = 256
NLN = "\n"
DKEYINOUT = { # Out/in, horizontal/vertical or row/col first.
("out",False): KEYROW,
("in",False): KEYCOL,
("out",True): KEYCOL,
("in",True): KEYROW,
}

ALLKEYS = [KEYCOMM,KEYROW, KEYCOL, KEYBASE, KEYPROMPT]
ALLALLKEYS = [KEYCOMM,KEYROW, KEYCOL, KEYBASE, KEYPROMPT, KEYBRK, "AND"]
fidentity = lambda x: x
ffloatd = lambda c: (lambda x: floatdef(x,c))
fcolourise = lambda: np.random.randint(0,MCOLOUR,size = 3)
fspace = lambda x: " {} ".format(x)



# Not modified functions
def split_l2(s, kr, kc, indsingles = False, fmap = fidentity, basestruct = None, indflip = False):
    """Split string to 2d list (ie L2) per row and col keys.
    
    The output is a list of lists, each of varying length.
    If a L2 basestruct is provided,
    will adhere to its structure using the following broadcast rules:
    - Basically matches row by row of base and new.
    - If a new row is shorter than base, the last value is repeated to fill the row.
    - If both are the same length, copied as is.
    - If new row is longer, then additional values will overflow to the next row.
      This might be unintended sometimes, but allows making all items col separated,
      then the new structure is simply adapted to the base structure.
    - If there are too many values in new, they will be ignored.
    - If there are too few values in new, the last one is repeated to fill base. 
    For mixed row + col ratios, singles flag is provided -
    will extract the first value of each row to a separate list,
    and output structure is (row L1,cell L2).
    There MUST be at least one value for row, one value for col when singles is on;
    to prevent errors, the row value is copied to col if it's alone (shouldn't affect results).
    Singles still respects base broadcast rules, and repeats its own last value.
    The fmap function is applied to each cell before insertion to L2;
    if it fails, a default value is used.
    If flipped, the keyword for columns is applied before rows.
    TODO: Needs to be a case insensitive split. Use re.split.
    """
    if indflip:
        tmp = kr
        kr = kc
        kc = tmp
    lret = []
    if basestruct is None:
        lrows = s.split(kr)
        lrows = [row.split(kc) for row in lrows]
        for r in lrows:
            cell = [fmap(x) for x in r]
            lret.append(cell)
        if indsingles:
            lsingles = [row[0] for row in lret]
            lcells = [row[1:] if len(row) > 1 else row for row in lret]
            lret = (lsingles,lcells)
    else:
        lrows = s.split(kr)
        r = 0
        lcells = []
        lsingles = []
        vlast = 1
        for row in lrows:
            row2 = row.split(kc)
            row2 = [fmap(x) for x in row2]
            vlast = row2[-1]
            indstop = False
            while not indstop:
                if (r >= len(basestruct) # Too many cell values, ignore.
                or (len(row2) == 0 and len(basestruct) > 0)): # Cell exhausted.
                    indstop = True
                if not indstop:
                    if indsingles: # Singles split.
                        lsingles.append(row2[0]) # Row ratio.
                        if len(row2) > 1:
                            row2 = row2[1:]
                    if len(basestruct[r]) >= len(row2): # Repeat last value.
                        indstop = True
                        broadrow = row2 + [row2[-1]] * (len(basestruct[r]) - len(row2))
                        r = r + 1
                        lcells.append(broadrow)
                    else: # Overfilled this row, cut and move to next.
                        broadrow = row2[:len(basestruct[r])]
                        row2 = row2[len(basestruct[r]):]
                        r = r + 1
                        lcells.append(broadrow)
        # If not enough new rows, repeat the last one for entire base, preserving structure.
        cur = len(lcells)
        while cur < len(basestruct):
            lcells.append([vlast] * len(basestruct[cur]))
            cur = cur + 1
        lret = lcells
        if indsingles:
            lsingles = lsingles + [lsingles[-1]] * (len(basestruct) - len(lsingles))
            lret = (lsingles,lcells)
    return lret
  
def is_l2(l):
    return isinstance(l[0],list) 

def l2_count(l):
    cnt = 0
    for row in l:
        cnt + cnt + len(row)
    return cnt
  
def list_percentify(l):
    """Convert each row in L2 to relative part of 100%. 
    
    Also works on L1, applying once globally.
    """
    lret = []
    if is_l2(l):
        for row in l:
            # row2 = [float(v) for v in row]
            row2 = [v / sum(row) for v in row]
            lret.append(row2)
    else:
        row = l[:]
        # row2 = [float(v) for v in row]
        row2 = [v / sum(row) for v in row]
        lret = row2
    return lret

def list_cumsum(l):
    """Apply cumsum to L2 per row, ie newl[n] = l[0:n].sum .
    
    Works with L1.
    Actually edits l inplace, idc.
    """
    lret = []
    if is_l2(l):
        for row in l:
            for (i,v) in enumerate(row):
                if i > 0:
                    row[i] = v + row[i - 1]
            lret.append(row)
    else:
        row = l[:]
        for (i,v) in enumerate(row):
            if i > 0:
                row[i] = v + row[i - 1]
        lret = row
    return lret

def list_rangify(l):
    """Merge every 2 elems in L2 to a range, starting from 0.  
    
    """
    lret = []
    if is_l2(l):
        for row in l:
            row2 = [0] + row
            row3 = []
            for i in range(len(row2) - 1):
                row3.append([row2[i],row2[i + 1]]) 
            lret.append(row3)
    else:
        row2 = [0] + l
        row3 = []
        for i in range(len(row2) - 1):
            row3.append([row2[i],row2[i + 1]]) 
        lret = row3
    return lret

def floatdef(x, vdef):
    """Attempt conversion to float, use default value on error.
    
    Mainly for empty ratios, double commas.
    """
    try:
        return float(x)
    except ValueError:
        print("'{}' is not a number, converted to {}".format(x,vdef))
        return vdef

def ratiosdealer(aratios2,aratios2r):
    aratios2 = list_percentify(aratios2)
    aratios2 = list_cumsum(aratios2)
    aratios2 = list_rangify(aratios2)
    aratios2r = list_percentify(aratios2r)
    aratios2r = list_cumsum(aratios2r)
    aratios2r = list_rangify(aratios2r)
    return aratios2,aratios2r


# MAIN Functions
def exchange(
  n
):
  n = n.replace(";", ",").replace(":", ",")
  return n

def visualize(
  mode, aratios, wo, ho, usecom, usebase, alpha, image=None, inprocess=False, rtl_template=False
):
  """make visually image by data. 
  
  this function was merged from Regional_prompter repository's makeimgtmp (in regions.py)
  """
  # :, ; をコンマに変換
  aratios = exchange(aratios)

  # 旧式に変更
  if mode == "Columns":
    mode = "Horizontal"
  if mode == "Rows":
    mode = "Vertical"
  indflip = ("Ver" in mode)
  
  
  if DELIMROW not in aratios: # Commas only - interpret as 1d.
      aratios2 = split_l2(aratios, DELIMROW, DELIMCOL, fmap = ffloatd(1), indflip = False)
      aratios2r = [1]
  else: # セミコロン ;
      (aratios2r,aratios2) = split_l2(aratios, DELIMROW, DELIMCOL, 
                                      indsingles = True, fmap = ffloatd(1), indflip = indflip)
  (aratios2,aratios2r) = ratiosdealer(aratios2,aratios2r)

  # リサイズ
  size = ho * wo
  if 262144 >= size: div = 4
  elif 1048576 >= size: div = 8
  else :div = 16
  h, w = ho // div, wo // div
  fx = np.zeros((h,w, 3), np.uint8)
  
  # Base image is coloured according to region divisions, roughly.
  for (i,ocell) in enumerate(aratios2r):
      for icell in aratios2[i]:
          # SBM Creep: Colour by delta so that distinction is more reliable.
          if not indflip:
              fx[int(h*ocell[0]):int(h*ocell[1]),int(w*icell[0]):int(w*icell[1]),:] = fcolourise()
          else:
              fx[int(h*icell[0]):int(h*icell[1]),int(w*ocell[0]):int(w*ocell[1]),:] = fcolourise()
  regions = PIL.Image.fromarray(fx)
  draw = ImageDraw.Draw(regions)
  c = 0
  def coldealer(col):
      if sum(col) > 380:return "black"
      else:return "white"
  # Add region counters at the top left corner, coloured according to hue.
  for (i,ocell) in enumerate(aratios2r):
      for icell in aratios2[i]: 
          if not indflip:
              draw.text((int(w*icell[0]),int(h*ocell[0])),f"{c}",coldealer(fx[int(h*ocell[0]),int(w*icell[0])]))
          else: 
              draw.text((int(w*ocell[0]),int(h*icell[0])),f"{c}",coldealer(fx[int(h*icell[0]),int(w*ocell[0])]))
          c += 1

  regions = regions.resize((wo, ho))

  if image is not None:
      regions = ImageChops.blend(regions, image, alpha)
  
  # Create ROW+COL template from regions.
  txtkey = fspace(DKEYINOUT[("in", indflip)]) + NLN  
  lkeys = [txtkey.join([""] * len(cell)) for cell in aratios2]
  txtkey = fspace(DKEYINOUT[("out", indflip)]) + NLN
  template = txtkey.join(lkeys) 
  if usebase:
      template = fspace(KEYBASE) + NLN + template
  if usecom:
      template = fspace(KEYCOMM) + NLN + template

  if inprocess:
      changer = template.split(NLN)
      changer = [l.strip() for l in changer]
      return changer
  
  print(f"[RP]: Template: {template}")
  
  if rtl_template:
    return regions, template
  return regions
