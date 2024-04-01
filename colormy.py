import icc
iccCoId = icc.icC
iccCoDId = icc.icCD
global output
global dnev
global text_dnev
text_dnev = ""
dnev = ""
global newVersion
newVersion = ""


def tic(text, color):

  itext = text
  icolor = color
  if icolor == "red":
    itext = f"\033[91m{itext}\033[91m"
    print(itext)
  elif icolor == "green":
    itext = f"\033[92m{itext}\033[92m"
    print(itext)
    itext = f"{itext}"
  elif icolor == "white":
    itext = f"\033[97m{itext}\033[97m"
    print(itext)
  elif icolor == "yellow":
    itext = f"\033[93m{itext}\033[93m"
    print(itext)

  else:
    if icolor == "":
      icolor = icolor.replace("", "null")
      print(f"$error No defined color: {icolor}")
  cmc()


def icc(iccCode=iccCoId):
  global output
  iccDCode = iccCoDId
  if iccCode == iccCoId:
    codeInput = input(":  ")
    if codeInput == "icc:default" or codeInput == "$=#":
      output = input()
    elif codeInput == "icc:green":
      mmcc("092")
      output = input()
    elif codeInput == "icc:red":
      mmcc("091")
      output = input()
    elif codeInput == "icc:white":
      output = input()
    elif codeInput == "icc:yellow":
      mmcc("093")
      output = input()
    cmc()
  elif iccCode == iccDCode:
    output = ""
    global dnev
    global text_dnev
    global text_color
    text_color = None
    if dnev == "icc:default" or dnev == "$=#":
      output = input()
    elif dnev == "icc:green":
      mmcc("092")
      output = input()
    elif dnev == "icc:red":
      mmcc("091")
      output = input()
    elif dnev == "icc:default":
      output = input()
    elif dnev == "icc:white":
      mmcc("097")
      output = input()
    elif dnev == "icc:yellow":
      mmcc("093")
      output = input()
    else:
      dnev = dnev.replace("icc:", "")
      print(f"$error No defined color: {dnev}")
    cmc()
    text_color = dnev.replace("icc:", "")
  else:
    print(f"$error No defined icc code: {iccCode}")


def cmc():
  print("\033[97m\033[97m")


def mmcc(colorForModify):
  if colorForModify == "092":
    print("\033[92m\033[92m")
  elif colorForModify == "091":
    print("\033[91m\033[91m")
  elif colorForModify == "097":
    print("\033[97m\033[97m")
  elif colorForModify == "093":
    print("\033[93m\033[93m")


def giveVariable(uCode=None, color=None):
  if "event.give" in uCode:
    if ".[doubleCode]" in uCode:
      double = "13960946"
      return double
    elif ".[singleCode]" in uCode:
      single = "6980473"
      return single
    elif ".[generatedIccCode]" in uCode:
      generatedIccCode = f"generated{color}"
      return generatedIccCode


def convertColorToIcc(color):
  globals()[f"converted{color}"] = f"icc:{color}"

  
  
