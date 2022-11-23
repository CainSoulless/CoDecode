import base64
import codecs

hashes = ["sha256"]


def encoders(hash, message):
    if hash == "sha256":
       return base64.b64encode(message) 


message = b"Hola"
en = encoders(hashes[0], message)

print(codecs.decode(en))

