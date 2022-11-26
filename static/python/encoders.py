import base64
import codecs
from cryptography.fernet import Fernet

# Testing
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


hashes = ["sha256"]

def enc_base64(message):
    output = base64.b64encode(str.encode(message))
    return output.decode("utf-8")
    
    
def enc_AES_CBC(message):
    key = get_random_bytes(32)
    cipher = AES.new(key, AES.MODE_CBC)
    ciphered_data = cipher.encrypt(pad(message, AES.block_size))
    return ciphered_data, key

# data, key = AES_CBC(plain_text)


def encoders(hash, message):
    if hash == "sha256":
       return base64.b64encode(message) 


def encrypt(message):
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(message)
    return token.decode("utf-8")
