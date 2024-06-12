import mysql.connector
from mysql.connector import Error
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64


class DatabaseAES:
    def __init__(self, key):
        self.key = key[:32]  #Ensure the key is 32 bytes for AES-256
        self.iv = b'mm\xcar\xe9\x85\x1dA,\xe1\x16\xb2\xa6\xe4\x97]'
    def encrypt(self, plain_text: str):
        try:
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            ct_bytes = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
            iv = base64.b64encode(self.iv).decode('utf-8')
            ct = base64.b64encode(ct_bytes).decode('utf-8')
            return f'{iv}:{ct}'
        except Exception as e:
            print(f"Encryption error: {e}")
            return None

    def decrypt(self, enc_text):
        try:
            iv, ct = enc_text.split(':')
            iv = base64.b64decode(iv)
            ct = base64.b64decode(ct)
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(ct), AES.block_size)
            return pt.decode('utf-8')
        except Exception as e:
            print(f"Decryption error: {e}")
            return None