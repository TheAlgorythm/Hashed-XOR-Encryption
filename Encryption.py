from bitarray import bitarray
import hashlib
import math
import secrets


class Encryption:

    _keyLength = 128

    @staticmethod
    def encrypt(message: bitarray, key: bitarray, difficulty=2) -> bitarray:
        keyLength = Encryption._keyLength
        iteratorKey = bitarray()
        iteratorSalt = bitarray()
        blockSalt = bitarray()
        if key.length() > keyLength + 2:
            iteratorSalt = key[keyLength + 1::2]
            blockSalt = key[keyLength + 2::2]
            iteratorKey = key[:keyLength]
        cypher = bitarray()
        blockSize = int(keyLength / difficulty)
        blocks = Encryption.sliceToBlocks(message, blockSize)
        for block in blocks:
            blockKey = Encryption.keyDerivation(iteratorKey, blockSalt, keyLength)
            iteratorKey = Encryption.keyDerivation(iteratorKey, iteratorSalt, keyLength)
            cypher.extend(block ^ blockKey[:block.length() * difficulty:difficulty])
        key = iteratorKey
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
        saltedKey = oldKey
        saltedKey.extend(salt)
        newKey.frombytes(hashlib.md5(saltedKey.tobytes()).digest())
        return newKey

    @staticmethod
    def generateKey(saltSize: int) -> bitarray:
        key = bitarray()
        key.frombytes(secrets.token_bytes(Encryption._keyLength + saltSize))
        return key
