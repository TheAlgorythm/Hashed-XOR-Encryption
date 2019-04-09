from bitarray import bitarray
import hashlib
import math


class Encryption:

    @staticmethod
    def encrypt(message: bitarray, key: bitarray, difficulty=2) -> bitarray:
        keyLength = 128
        salt = bitarray()
        if key.length() > keyLength:
            salt = key[keyLength + 1:]
            key = key[:keyLength]
        cypher = bitarray()
        blockSize = int(keyLength / difficulty)
        blocks = Encryption.sliceToBlocks(message, blockSize)
        for block in blocks:
            key = Encryption.keyDerivation(key, salt, keyLength)
            Encryption.addToList(cypher, block ^ key[:block.length() * difficulty:difficulty])
        return cypher
    
    @staticmethod
    def sliceToBlocks(iterList: bitarray, blockSize: int) -> list:
        blocks = list()
        listLength = iterList.length()
        blockCount = math.ceil(listLength / blockSize)
        for i in range(0, blockCount):
            stop = (i + 1) * blockSize
            if stop > listLength:
                stop = listLength
            blocks.append(iterList[i * blockSize:stop])
        return blocks

    @staticmethod
    def keyDerivation(oldKey: bitarray, salt: bitarray, length: int) -> bitarray:
        newKey = bitarray()
        saltedKey = bitarray(oldKey)
        Encryption.addToList(saltedKey, salt)
        newKey.frombytes(hashlib.md5(saltedKey.tobytes()).digest())
        return newKey

    @staticmethod
    def addToList(iterList, appending):
        for item in appending:
            iterList.append(item)

