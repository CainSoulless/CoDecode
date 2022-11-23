import base64
import codecs
from cryptography.fernet import Fernet

hashes = ["sha256"]


def encoders(hash, message):
    if hash == "sha256":
       return base64.b64encode(message) 


def encrypt(message):
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(message)
    return token.decode("utf-8")
