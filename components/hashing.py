from hashlib import sha512, sha256, md5, sha1
from eth_utils import keccak
from toolbox import byte

def hash(algo, plaintext):
  if algo == "SHA-1":
    returm sha1(byte(plaintext)).hexdigest()
  elif algo == "Keccak-256":
    return keccak(byte(plaintext)).hex()
  elif algo == "SHA-256":
    return sha256(byte(plaintext)).hexdigest()
  elif algo == "MD5":
    return md5(byte(plaintext)).hexdigest()
  elif algo == "SHA-1":
    return sha1(byte(plaintext)).hexdigest()
