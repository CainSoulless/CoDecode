import base64
from cryptography.fernet import Fernet

# Crypto 
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Protocol.KDF import PBKDF2


def encode_option(encode_option, message):
    if encode_option == "Plain":
        return message
    elif encode_option == "base64":
        return base64.b64encode(str.encode(message)).decode("utf-8")
    elif encode_option == "AES_EAX":
        nonce, output, tag = enc_AES_EAX(message)
        return nonce, output, tag


def random_key():
    return get_random_bytes(32)


def enc_AES_EAX(message, key):
    cipher = AES.new(base64.b64decode(key), AES.MODE_EAX)
    nonce = cipher.nonce
    ciphered, tag = cipher.encrypt_and_digest(message.encode("ascii"))
    b64_ciphered = base64.b64encode(ciphered).decode("utf-8")
    b64_nonce = base64.b64encode(nonce).decode("utf-8")
    b64_tag = base64.b64encode(tag).decode("utf-8")

    return b64_nonce, b64_ciphered, b64_tag


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
