import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter

BS = 32
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
unpad = lambda s : s[0:-ord(s[-1:])]

class AESCipher(object):

    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw, mode):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)


        cipher = {
            'CBC': AES.new(self.key, AES.MODE_CBC, iv),
            'ECB': AES.new(self.key, AES.MODE_ECB),
            'CFB': AES.new(self.key, AES.MODE_CFB, iv),
            'OFB': AES.new(self.key, AES.MODE_OFB, iv),
            'CTR': AES.new(self.key, AES.MODE_CTR, counter=Counter.new(128)),
        }.get(mode, AES.new(self.key, AES.MODE_CBC, iv))

        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc, mode):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]

        cipher = {
            'CBC': AES.new(self.key, AES.MODE_CBC, iv),
            'ECB': AES.new(self.key, AES.MODE_ECB),
            'CFB': AES.new(self.key, AES.MODE_CFB, iv),
            'OFB': AES.new(self.key, AES.MODE_OFB, iv),
            'CTR': AES.new(self.key, AES.MODE_CTR, counter=Counter.new(128)),
        }.get(mode, AES.new(self.key, AES.MODE_CBC, iv))
        return unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

