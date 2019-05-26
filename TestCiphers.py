from AESCipher import AESCipher
from DES3Cipher import DES3Cipher
import time, os

cipherEncFunctions = {
    0: lambda cipher, plaintext: cipher.encrypt(plaintext, 'CBC'),
    1: lambda cipher, plaintext: cipher.encrypt(plaintext, 'ECB'),
    2: lambda cipher, plaintext: cipher.encrypt(plaintext, 'CFB'),
    3: lambda cipher, plaintext: cipher.encrypt(plaintext, 'OFB'),
    4: lambda cipher, plaintext: cipher.encrypt(plaintext, 'CTR'),
}
cipherDecFunctions = {
    0: lambda cipher, cipherText: cipher.decrypt(cipherText, 'CBC'),
    1: lambda cipher, cipherText: cipher.decrypt(cipherText, 'ECB'),
    2: lambda cipher, cipherText: cipher.decrypt(cipherText, 'CFB'),
    3: lambda cipher, cipherText: cipher.decrypt(cipherText, 'OFB'),
    4: lambda cipher, cipherText: cipher.decrypt(cipherText, 'CTR'),
}

def openTestingFiles():
    global smallFile
    global mediumFile
    global largeFile
    global rawOutputFile

    smallFile = open(os.path.join(os.path.dirname(__file__), "testdata/1MB/dummy.txt"), "r")
    mediumFile = open(os.path.join(os.path.dirname(__file__), "testdata/128MB/dummy.txt"), "r")
    largeFile = open(os.path.join(os.path.dirname(__file__), "testdata/1GB/dummy.txt"), "r")
    rawOutputFile = open(os.path.join(os.path.dirname(__file__), "output/raw.txt"), "w")


def testAES():
    aesCipher = AESCipher('aaaaaaqweqweqweasdawqawqswqawews') # 32 bit key
    i = 0
    while i < 5:
        t = time.perf_counter()
        cipher = cipherEncFunctions[i](aesCipher, smallFile.read()) # encrypt the file
        cipherDecFunctions[i](aesCipher, cipher) # decrypt the file
        print("Time elapsed: " + str(time.perf_counter() - t))
        i+=1

def testDES3():
    des3Cipher = DES3Cipher('aaaaaaqweqweqwea') # 16 bit key
    i = 0
    while i < 5:
        t = time.perf_counter()
        cipher = cipherEncFunctions[i](des3Cipher, smallFile.read()) # encrypt the file
        cipherDecFunctions[i](des3Cipher, cipher) # decrypt the file
        print("Time elapsed: " + str(time.perf_counter() - t))
        i+=1

openTestingFiles()
testAES()
testDES3()
