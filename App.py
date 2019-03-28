import sys
from bitarray import bitarray
from Encryption import Encryption
from datetime import datetime


class App:
    @staticmethod
    def exec(argv):
        message = bitarray()
        with open(argv[1], 'rb') as fh:
            message.fromfile(fh)

        key = bitarray()
        with open(argv[2], 'rb') as fh:
            key.fromfile(fh)
        
        start_time = datetime.now()

        encrypted = Encryption.encrypt(message, key)

        time_elapsed = datetime.now() - start_time
        print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))

        with open(argv[3], 'wb') as fh:
            encrypted.tofile(fh)


if __name__ == '__main__':
    App.exec(sys.argv)
