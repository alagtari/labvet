import base64


with open("code_a_barre.png" , "rb") as f:


    encoded_string= base64.b64encode(f.read())
    print(encoded_string.decode('utf-8'))