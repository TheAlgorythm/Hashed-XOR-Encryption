# Hashed-XOR-Encryption

The concept behind this encryption you can find [here](Concept.md).

## Usage

```shell
usage: App.py [-h] {Crypt,Generate} ...

Hashed XOR Encryption

optional arguments:
  -h, --help        show this help message and exit

commands:
  {Crypt,Generate}
    Crypt           Encrypt/Decrypt Files
        Usage: App.py Crypt [-h] Sourcefile Keyfile Destinationfile
    Generate        Generate Keyfile
        Usage: App.py Generate [-h] Keyfile Saltsize
```

## For Testing:

```shell
$ pipenv install
$ pipenv run python App.py Crypt lorem.txt first.key encrypted.crypt
$ pipenv run python App.py Crypt encrypted.crypt first.key decrypted.txt
$ nano decrypted.txt
```

To generate and diff test files you can use my tool [FileSet](https://github.com/TheAlgorythm/FileSet).
