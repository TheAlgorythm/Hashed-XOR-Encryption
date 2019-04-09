import argparse
from bitarray import bitarray
from Encryption import Encryption
from datetime import datetime


class App:

    @staticmethod
    def argumentParser():
        parser = argparse.ArgumentParser(description='Hashed XOR Encryption')

        subparsers = parser.add_subparsers(title="commands", dest="command")
        cryptParser = subparsers.add_parser("Crypt", help="Encrypt/Decrypt Files")

        cryptParser.add_argument('Sourcefile', type=argparse.FileType('rb'))
        cryptParser.add_argument('Keyfile', type=argparse.FileType('rb'))
        cryptParser.add_argument('Destinationfile', type=argparse.FileType('wb'))

        generateParser = subparsers.add_parser("Generate", help="Generate Keyfile")

        generateParser.add_argument('Keyfile', type=argparse.FileType('wb'))
        generateParser.add_argument('Saltsize', type=int)

        return parser.parse_args()

    @staticmethod
    def exec(argv):
        if argv.command == "Crypt":
            App.crypt(argv)
        elif argv.command == "Generate":
            App.generate(argv)
    
    @staticmethod
    def crypt(argv):
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
    
    @staticmethod
    def generate(argv):
        key = Encryption.generateKey(argv.Saltsize)

        with argv.Keyfile as fh:
            key.tofile(fh)


if __name__ == '__main__':
    args = App.argumentParser()
    App.exec(args)
