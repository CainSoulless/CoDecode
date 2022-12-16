import base64
# Crypto 
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Protocol.KDF import PBKDF2


def random_key():
    return get_random_bytes(32)


def enc_AES_EAX(message, key):
    cipher = AES.new(base64.b64decode(key), AES.MODE_EAX)
    nonce = cipher.nonce
    ciphered, tag = cipher.encrypt_and_digest(message.encode("ascii"))
    b64_ciphered = base64.b64encode(ciphered).decode("utf-8")
    b64_nonce = base64.b64encode(nonce).decode("utf-8")
    b64_tag = base64.b64encode(tag).decode("utf-8")

    return b64_ciphered, b64_nonce, b64_tag


# def dec_AES_EAX(message, key, nonce, tag):
#     message = base64.b64decode(message)
#     key = base64.b64decode(key)
#     nonce = base64.b64decode(nonce)
#     tag = base64.b64decode(tag)
#     print(message, key, nonce, tag)

#     cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
#     plain = cipher.decrypt(message)
#     try:
#         cipher.verify(tag)
#         return plain.decode("ascii")
#     except:
#         return False


def dec_AES_EAX(ciphered, key, nonce, tag):
    ciphered = base64.b64decode(ciphered)
    key = base64.b64decode(key)
    nonce = base64.b64decode(nonce)
    tag = base64.b64decode(tag)
    print(ciphered)
    print(key)
    print(nonce)
    print(tag)
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plain = cipher.decrypt(ciphered)
    try:
        cipher.verify(tag)
        return plain.decode("ascii")
    except:
        return False

message = "O7h9cA=="
key = "MT4CnTPAgCtVt89cv9Ahom/OmvKMLor9GE7xqPoEesU="
nonce = "0k/gIINPf79z5OLhYfQF6A=="
tag = "vLygzeWR6RY/vMiflMl9lA=="

output = dec_AES_EAX(message, key, nonce, tag)
print(output)

print("1)Generate key\n2)Encode\n3)Decode\n")
option = int(input("Option: "))

if option == 1:
    key = base64.b64encode(get_random_bytes(32)).decode("utf-8")
    print(key)
    exit()
elif option == 2:
    message = input("Message: ")
    # message = "Hola"
    key = input("key: ")
    output, nonce, tag = enc_AES_EAX(message, key)
    print(output)
    print(nonce)
    print(tag)
elif option == 3:
    message = input("message: ") 
    # message = "O7h9cA=="
    key = input("key: ")
    nonce = input("nonce: ")
    tag = input("tag: ")

    output = dec_AES_EAX(message, key, nonce, tag)
    print(output)