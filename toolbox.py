from pathlib import Path
import json, copy, os

with open("config.json", "r") as r:
  config = json.load(r)

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def parse(name):
  if name == "dictionary":
    with open(f"{Path(__file__).parent}/{config['directories']['datasets']['dictionary']['english']}", "r") as r:
      en = json.load(r)
    with open(f"{Path(__file__).parent}/{config['directories']['datasets']['dictionary']['romanian']}", "r") as r:
      ro = json.load(r)
    with open(f"{Path(__file__).parent}/{config['directories']['datasets']['dictionary']['portuguese']}", "r") as r:
      pt = json.load(r)
    with open(f"{Path(__file__).parent}/{config['directories']['datasets']['dictionary']['spanish']}", "r") as r:
      es = json.load(r)
    with open(f"{Path(__file__).parent}/{config['directories']['datasets']['dictionary']['chinese']}", "r") as r:
      zh = json.load(r)
    with open(f"{Path(__file__).parent}/{config['directories']['datasets']['dictionary']['italian']}", "r") as r:
      it = json.load(r)
    with open(f"{Path(__file__).parent}/{config['directories']['datasets']['dictionary']['french']}", "r") as r:
      fr = json.load(r)
    return en + ro + pt + es + zh + it + fr
  elif name == "dataBreach":
    with open(f"{Path(__file__).parent}/{config['directories']['datasets']['dataBreaches']['crackedHashes']}", "r") as r:
      ch = json.load(r)
    with open(f"{Path(__file__).parent}/{config['directories']['datasets']['dataBreaches']['usernames']}", "r") as r:
      us = json.load(r)
    with open(f"{Path(__file__).parent}/{config['directories']['datasets']['dataBreaches']['passwords']['part1']}", "r") as r:
      p1 = json.load(r)
    with open(f"{Path(__file__).parent}/{config['directories']['datasets']['dataBreaches']['passwords']['part2']}", "r") as r:
      p2 = json.load(r)
    with open(f"{Path(__file__).parent}/{config['directories']['datasets']['dataBreaches']['passwords']['part3']}", "r") as r:
      p3 = json.load(r)
    with open(f"{Path(__file__).parent}/{config['directories']['datasets']['dataBreaches']['passwords']['part4']}", "r") as r:
      p4 = json.load(r)
    return ch + us + p1 + p2 + p3 + p4
  else:
    return False

def template(path):
  with open(path, "r") as r:
    return copy.deepcopy(json.load(r))

def byte(inp):
  hexadecimal = None
  try:
    bytes.fromhex(inp)
    hexadecimal = True
  except:
    hexadecimal = False

  if isinstance(inp, int):
    return inp.to_bytes((inp.bit_length() + 7) // 8, "big")
  elif isinstance(inp, str) and hexadecimal == False:
    return inp.encode("utf-8")
  elif isinstance(inp, bool) or inp == None:
    return str(inp).encode("utf-8")
  elif isinstance(inp, list):
    return b"".join(inp)
  elif hexadecimal:
    return bytes.fromhex(inp)
