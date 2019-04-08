from bitarray import bitarray
import hashlib
import math


class Encryption:

    @staticmethod
    def encrypt(message: bitarray, key: bitarray, difficulty=2) -> bitarray:
        cypher = bitarray()
        keyLength = 128
        blockSize = int(keyLength / difficulty)
        blocks = Encryption.sliceToBlocks(message, blockSize)
        for block in blocks:
            key = Encryption.keyDerivation(key, keyLength)
            Encryption.addToList(cypher, block ^ key[:block.length() * difficulty:difficulty])
        return cypher
    
    @staticmethod
    def sliceToBlocks(iterList: bitarray, blockSize: int) -> list:
        blocks = list()
        listLength = len(iterList)
        blockCount = math.ceil(listLength / blockSize)
        for i in range(0, blockCount):
            stop = (i + 1) * blockSize
            if stop > listLength:
                stop = listLength
            blocks.append(iterList[i * blockSize:stop])
        return blocks

    @staticmethod
    def keyDerivation(oldKey: bitarray, length: int) -> bitarray:
        newKey = bitarray()
        newKey.frombytes(hashlib.md5(oldKey.tobytes()).digest())
        return newKey

    @staticmethod
    def addToList(iterList, appending):
        for item in appending:
            iterList.append(item)

