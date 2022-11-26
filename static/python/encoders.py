import base64
import codecs
from cryptography.fernet import Fernet

# Testing
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Protocol.KDF import PBKDF2

def enc_base64(message):
    output = base64.b64encode(str.encode(message))
    return output.decode("utf-8")


key = get_random_bytes(32)

def enc_AES_EAX(message):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphered, tag = cipher.encrypt_and_digest(message.encode("ascii"))
    b64_ciphered = base64.b64encode(ciphered).decode("utf-8")
    return nonce, b64_ciphered, tag


"""
Testing purposes. Don't delete until the code is passed to decoder.py 
"""
# def dec_AES_EAX(nonce, ciphered, tag):
#     ciphered = base64.b64decode(ciphered)
#     cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
#     plain = cipher.decrypt(ciphered)
#     try:
#         cipher.verify(tag)
#         return plain.decode("ascii")
#     except:
#         return False
#
#
# nonce, encoded, tag = enc_AES_EAX("Hola")
# print(encoded)
# print(dec_AES_EAX(nonce, encoded, tag))

def encrypt(message):
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(message)
    return token.decode("utf-8")
