import base64

def decode_option(encode_option, message):
    if encode_option == "Plain":
        return message
    elif encode_option == "base64":
        return base64.b64decode(str.encode(message)).decode("utf-8")