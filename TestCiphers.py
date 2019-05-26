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

dummyFiles = {
    0: open(os.path.join(os.path.dirname(__file__), "testdata/1MB/dummy.txt"), "r").read(),
    1: open(os.path.join(os.path.dirname(__file__), "testdata/128MB/dummy.txt"), "r").read(),
    2: open(os.path.join(os.path.dirname(__file__), "testdata/1MB/dummy.txt"), "r").read()
}


def openTestingFiles():
    global rawOutputFile
    rawOutputFile = open(os.path.join(os.path.dirname(__file__), "raw_output/raw.txt"), "w")


def writeRawOutput(timeToEncrypt, timeToDecrypt, cipherName, cipherBlockModeIndex, fileSizeIndex):
    fileSizes = {
        0: "1MB",
        1: "128MB",
        2: "1GB"
    }
    cipherBlockModes = {
        0: "CBC",
        1: "ECB",
        2: "CFB",
        3: "OFB",
        4: "CTR"
    }

    rawOutputFile.write(
        "Time to encrypt with: " + cipherName + ":" + cipherBlockModes[cipherBlockModeIndex] + ":" + fileSizes[
            fileSizeIndex] + " = " + str(timeToEncrypt) + "\n")
    rawOutputFile.write(
        "Time to decrypt with: " + cipherName + ":" + cipherBlockModes[cipherBlockModeIndex] + ":" + fileSizes[
            fileSizeIndex] + " = " + str(timeToDecrypt) + "\n")


def testAES():
    aesCipher = AESCipher('aaaaaaqweqweqweasdawqawqswqawews')  # 32 bit key
    i = 0
    while i < 5:  # Run each scenario 5 times
        for cipherEncDictKey, cipherEncDictValue in cipherEncFunctions.items():
            for fileKey, fileValue in dummyFiles.items():
                t = time.perf_counter()
                cipher = cipherEncDictValue(aesCipher, fileValue)  # Encrypt the file
                timeToEncrypt = time.perf_counter() - t
                cipherDecFunctions[cipherEncDictKey](aesCipher, cipher)  # Decrypt the file
                timeToDecrypt = time.perf_counter() - timeToEncrypt
                writeRawOutput(timeToEncrypt, timeToDecrypt, "aes", cipherEncDictKey, fileKey)
        i += 1

def testDES3():
    des3Cipher = DES3Cipher('aaaaaaqweqweqwea')  # 16 bit key
    i = 0
    while i < 5:  # Run each scenario 5 times
        for cipherEncDictKey, cipherEncDictValue in cipherEncFunctions.items():
            for fileKey, fileValue in dummyFiles.items():
                t = time.perf_counter()
                cipher = cipherEncDictValue(des3Cipher, fileValue)  # Encrypt the file
                timeToEncrypt = time.perf_counter() - t
                cipherDecFunctions[cipherEncDictKey](des3Cipher, cipher)  # Decrypt the file
                timeToDecrypt = time.perf_counter() - timeToEncrypt
                writeRawOutput(timeToEncrypt, timeToDecrypt, "3des", cipherEncDictKey, fileKey)
        i += 1
    rawOutputFile.close()


openTestingFiles()
testAES()
testDES3()
