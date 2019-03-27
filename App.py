import sys
from bitarray import bitarray
from Encryption import Encryption


class App:
    @staticmethod
    def exec(argv):
        message = bitarray()
        #message.fromstring(argv[1])
        with open(argv[1], 'rb') as fh:
            message.fromfile(fh)
        key = bitarray()
        #key.fromstring(argv[2])
        with open(argv[2], 'rb') as fh:
            key.fromfile(fh)
        encrypted = Encryption.encrypt(message, key)
        with open(argv[3], 'wb') as fh:
            encrypted.tofile(fh)


if __name__ == '__main__':
    App.exec(sys.argv)
