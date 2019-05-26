import base64
import hashlib
from Crypto.Cipher import DES3
from Crypto import Random
from Crypto.Util import Counter

BS = 8
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
unpad = lambda s : s[0:-ord(s[-1:])]

class DES3Cipher(object):

    def __init__(self, key):
        self.key = key

    def encrypt(self, raw, mode):
        raw = pad(raw)
        iv = Random.new().read(DES3.block_size)
        cipher = {
            'CBC': DES3.new(self.key, DES3.MODE_CBC, iv),
            'ECB': DES3.new(self.key, DES3.MODE_ECB),
            'CFB': DES3.new(self.key, DES3.MODE_CFB, iv),
            'OFB': DES3.new(self.key, DES3.MODE_OFB, iv),
            'CTR': DES3.new(self.key, DES3.MODE_CTR, counter=Counter.new(64)),
        }.get(mode, DES3.new(self.key, DES3.MODE_CBC, iv))
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc, mode):
        enc = base64.b64decode(enc)
        iv = enc[:DES3.block_size]
        cipher = {
            'CBC': DES3.new(self.key, DES3.MODE_CBC, iv),
            'ECB': DES3.new(self.key, DES3.MODE_ECB),
            'CFB': DES3.new(self.key, DES3.MODE_CFB, iv),
            'OFB': DES3.new(self.key, DES3.MODE_OFB, iv),
            'CTR': DES3.new(self.key, DES3.MODE_CTR, counter=Counter.new(64)),
        }.get(mode, DES3.new(self.key, DES3.MODE_CBC, iv))
        return unpad(cipher.decrypt(enc[DES3.block_size:])).decode('utf-8')
