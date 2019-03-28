from bitarray import bitarray
import hashlib
import math


class Encryption:

    @staticmethod
    def encrypt(message, key, difficulty=2):
        cypher = bitarray()
        keyLength = 128
        blockSize = int(keyLength / difficulty)
        blocks = Encryption.sliceToBlocks(message, blockSize)
        for block in blocks:
            newKey = bitarray()
            newKey.frombytes(Encryption.keyDerivation(key, keyLength))
            Encryption.addToList(cypher, block ^ newKey[:block.length() * difficulty:difficulty])
            key = newKey
        return cypher
    
    @staticmethod
    def sliceToBlocks(iterList, blockSize):
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
    def keyDerivation(oldKey, length):
        return hashlib.md5(oldKey.tobytes()).digest()

    @staticmethod
    def addToList(iterList, appending):
        for item in appending:
            iterList.append(item)

