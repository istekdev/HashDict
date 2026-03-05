from components import backend
from termcolor import colored
import os, time, json, sys
from toolbox import clear
from pathlib import Path

with open(f"{Path(__file__).parent.parent}/config.json", "r") as r:
  config = json.load(r)

def menu():
  title, data, options = """
██╗░░██╗░█████╗░░██████╗██╗░░██╗██████╗░██╗░█████╗░████████╗
██║░░██║██╔══██╗██╔════╝██║░░██║██╔══██╗██║██╔══██╗╚══██╔══╝
███████║███████║╚█████╗░███████║██║░░██║██║██║░░╚═╝░░░██║░░░
██╔══██║██╔══██║░╚═══██╗██╔══██║██║░░██║██║██║░░██╗░░░██║░░░
██║░░██║██║░░██║██████╔╝██║░░██║██████╔╝██║╚█████╔╝░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░░░░╚═╝░░░""", f"Version: {str(config["metadata"]["version"])}\nDev: {config["metadata"]["developer"]}\nGithub: {config["metadata"]["github"]}", "[N] - New Rainbow Table\n[X] - Exit"
  print(colored(title, "red", attrs=["bold"]))
  print(colored(f"\n--\n{data}\n--\n{options}\n", "white", attrs=["bold"]))
  print(colored("[X] - Exit\n\n", "red", attrs=["bold"]))
  option = input(colored(">>> ", "white", attrs=["bold"]))
  if option.upper() in ["X", "[X]"]:
    sys.exit(0)
  elif option.upper() in ["N", "[N]"]:
    clear()
    print(colored("Select Hashing Algorithm:\n\n[SHA-256]\n[SHA-512]\n[KECCAK-256]\n[MD5]\n[SHA-1]\n\n", "white", attrs=["bold"]))
    algo = input(colored(">>> ", "white", attrs=["bold"]))
    if config["info"]["hashMonitor"] == False:
      print(colored("Hashing Rainbow Table...", "yellow", attrs=["bold"]))
    new(algo)
    time.sleep(3)
    clear()
    menu()
  else:
    print(colored("Error - Invalid Command. Returning in 3 Seconds...", "red", attrs=["bold"]))
    time.sleep(3)
    clear()
    menu()
