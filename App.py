import argparse
from bitarray import bitarray
from Encryption import Encryption
from datetime import datetime


class App:

    @staticmethod
    def argumentParser():
        parser = argparse.ArgumentParser(description='Encrypt/Decrypt Files')

        parser.add_argument('Sourcefile', type=argparse.FileType('rb'))
        parser.add_argument('Keyfile', type=argparse.FileType('rb'))
        parser.add_argument('Destinationfile', type=argparse.FileType('wb'))

        return parser

    @staticmethod
    def exec(argv):
        message = bitarray()
        with argv.Sourcefile as fh:
            message.fromfile(fh)

        key = bitarray()
        with argv.Keyfile as fh:
            key.fromfile(fh)
        
        start_time = datetime.now()

        encrypted = Encryption.encrypt(message, key)

        time_elapsed = datetime.now() - start_time
        print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))

        with argv.Destinationfile as fh:
            encrypted.tofile(fh)


if __name__ == '__main__':
    parser = App.argumentParser()
    args = parser.parse_args()
    App.exec(args)
