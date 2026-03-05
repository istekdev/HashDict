import json, copy

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
