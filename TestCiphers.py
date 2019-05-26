from AESCipher import AESCipher
from DES3Cipher import DES3Cipher
import time

cipherEncFunctions = {
    0: lambda cipher: cipher.encrypt('Testing CBC', 'CBC'),
    1: lambda cipher: cipher.encrypt('Testing ECB', 'ECB'),
    2: lambda cipher: cipher.encrypt('Testing CFB', 'CFB'),
    3: lambda cipher: cipher.encrypt('Testing OFB', 'OFB'),
    4: lambda cipher: cipher.encrypt('Testing CTR', 'CTR'),
}
cipherDecFunctions = {
    0: lambda cipher, cipherText: cipher.decrypt(cipherText, 'CBC'),
    1: lambda cipher, cipherText: cipher.decrypt(cipherText, 'ECB'),
    2: lambda cipher, cipherText: cipher.decrypt(cipherText, 'CFB'),
    3: lambda cipher, cipherText: cipher.decrypt(cipherText, 'OFB'),
    4: lambda cipher, cipherText: cipher.decrypt(cipherText, 'CTR'),
}

def testAES():
    aesCipher = AESCipher('aaaaaaqweqweqweasdawqawqswqawews') # 32 bit key
    i = 0
    while i < 5:
        t = time.perf_counter()
        cipher = cipherEncFunctions[i](aesCipher)
        print(cipher)
        print(cipherDecFunctions[i](aesCipher, cipher))
        print("Time elapsed: " + str(time.perf_counter() - t))
        i+=1

def testDES3():
    des3Cipher = DES3Cipher('aaaaaaqweqweqwea') # 16 bit key
    i = 0
    while i < 5:
        cipher = cipherEncFunctions[i](des3Cipher)
        print(cipher)
        print(cipherDecFunctions[i](des3Cipher, cipher))
        i+=1

testAES()
testDES3()
