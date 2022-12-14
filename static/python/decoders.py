import base64

# Crypto 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Protocol.KDF import PBKDF2

def decode_option(encode_option, message):
    if encode_option == "Plain":
        return message
    elif encode_option == "base64":
        return base64.b64decode(str.encode(message)).decode("utf-8")


# def dec_AES_EAX(message, key, nonce, tag):
#     message = base64.b64decode(message)
#     cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
#     plain = cipher.decrypt(ciphered)
#     try:
#         cipher.verify(tag)
#         return plain.decode("ascii")
#     except:
#         return False




# def decc_AES_EAX(message, key):
def dec_AES_EAX(message, key, nonce, tag):
    cipher = AES.new(base64.b64decode(key), AES.MODE_EAX)
    nonce = cipher.nonce
    ciphered, tag = cipher.encrypt_and_digest(message.encode("ascii"))
    b64_ciphered = base64.b64encode(ciphered).decode("utf-8")
    b64_nonce = base64.b64encode(nonce).decode("utf-8")
    b64_tag = base64.b64encode(tag).decode("utf-8")

    return b64_nonce, b64_ciphered, b64_tag


# print(dec_AES_EAX())