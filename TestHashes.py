import hashlib, os, time

def writeOutput(outputFile, timeToEncode, hashName):
    outputFile.write(hashName + ":" + str(timeToEncode) + "\n")


def encodeAndTime(rawOutputFile):
    testString = "TestDATA"


    t = time.perf_counter()
    hashlib.md5(testString.encode())
    timeToEncode = time.perf_counter() - t
    writeOutput(rawOutputFile, timeToEncode, "MD5")

    t = time.perf_counter()
    hashlib.sha256(testString.encode())
    timeToEncode = time.perf_counter() - t
    writeOutput(rawOutputFile, timeToEncode, "SHA256")

    t = time.perf_counter()
    hashlib.sha384(testString.encode())
    timeToEncode = time.perf_counter() - t
    writeOutput(rawOutputFile, timeToEncode, "SHA384")

    t = time.perf_counter()
    hashlib.sha224(testString.encode())
    timeToEncode = time.perf_counter() - t
    writeOutput(rawOutputFile, timeToEncode, "SHA224")

    t = time.perf_counter()
    hashlib.sha512(testString.encode())
    timeToEncode = time.perf_counter() - t
    writeOutput(rawOutputFile, timeToEncode, "SHA512")

    t = time.perf_counter()
    hashlib.sha1(testString.encode())
    timeToEncode = time.perf_counter() - t
    writeOutput(rawOutputFile, timeToEncode, "SHA1")

    rawOutputFile.write("\n")

def runTestNTimes(n):
    rawOutputFile = open(os.path.join(os.path.dirname(__file__), "raw_output/raw_hash.txt"), "w")
    i = 0
    while i < n:
        encodeAndTime(rawOutputFile)
        i+=1
    rawOutputFile.close()

runTestNTimes(10)