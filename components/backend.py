from hashlib import sha512, sha256, md5, sha1
from toolbox import byte, template, parse
import os, json, time, base58, sys
from termcolor import colored
from eth_utils import keccak
from pathlib import Path

with open(f"{Path(__file__).parent.parent}/config.json", "r") as r:
  config = json.load(r)
hashEntry, hashComp = template(f"{Path(__file__).parent.parent}/{config['directories']['templates']['hashEntry']}"), template(f"{Path(__file__).parent.parent}/{config['directories']['templates']['hashComp']}")
dictionary, dataBreach = parse("dictionary"), parse("dataBreach")

def hash(algo, plaintext):
  if algo == "SHA-1":
    return sha1(byte(plaintext)).hexdigest()
  elif algo == "Keccak-256":
    return keccak(byte(plaintext)).hex()
  elif algo == "SHA-256":
    return sha256(byte(plaintext)).hexdigest()
  elif algo == "MD5":
    return md5(byte(plaintext)).hexdigest()

def new(algo):
  if algo not in config["info"]["supportedHashAlgo"]:
    print(colored("Error - Invalid Hashing Function. Exiting in 3 Seconds...", "red", attrs=["bold"]))
    time.sleep(3)
    sys.exit(1)
  os.makedirs(f"{Path(__file__).parent.parent}/{config['directories']['output']}", exist_ok=True)
  dictionaryCount, dataBreachCount = 0, 0

  hashEntry["metadata"]["version"], hashEntry["metadata"]["timestamp"], hashEntry["metadata"]["hashFunc"] = int(config["metadata"]["version"]), round(time.time()), algo
  id = base58.b58encode(os.urandom(24)).decode()
  with open(f"{Path(__file__).parent.parent}/{config['directories']['output']}/output_{id}.json", "w") as w:
    json.dump(hashEntry, w, indent=4)

  with open(f"{Path(__file__).parent.parent}/{config['directories']['output']}/output_{id}.json", "r") as r:
    entry = json.load(r)
  chunks = []

  for text in dictionary:
    dictionaryCount += 1
    output = hash(algo, text)

    hashComp["input"], hashComp["output"] = text, output
    chunk.append(hashComp.copy())
    if len(chunk) >= 10000:
      entry["table"].append(chunk)
      with open(f"{Path(__file__).parent.parent}/{config['directories']['output']}/output_{id}.json", "w") as w:
        json.dump(entry, w, indent=4)
      chunks.clear()
    if config["info"]["hashMonitor"]:
      print(colored(f"Dictionary Hash #{str(dictionaryCount)} - {output}", "yellow", attrs=["bold"]))
  for text in dataBreach:
    dataBreachCount += 1
    output = hash(algo, text)

    hashComp["input"], hashComp["output"] = text, output
    chunk.append(hashComp.copy())
    if len(chunk) >= 10000:
      entry["table"].append(chunk)
      with open(f"{Path(__file__).parent.parent}/{config['directories']['output']}/output_{id}.json", "w") as w:
        json.dump(entry, w, indent=4)
      chunks.clear()
    if config["info"]["hashMonitor"]:
      print(colored(f"Data Breach Hash #{str(dictionaryCount)} - {output}", "yellow", attrs=["bold"]))
  
  print(colored(f"Saved Successfully as {Path(__file__).parent.parent}/{config['directories']['output']}/output_{id}.json", "green", attrs=["bold"]))
