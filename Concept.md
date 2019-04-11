# Concept

## Python like Pseudo-Code

```python
def encrypt(message, key, difficulty=2):
  for block in message:
    newKey = hash(key)
    encrypted += block ^ newKey[::difficulty]
    key = newKey
```

## Security

- parts of key stay private and are not used for encryption but only for hashing (key derivation)
- Threre is no possiblility to recalculate the keys before hashing, because even the hashes are secret
- a part of salt should be a secret for a higher entropy. The other part could be public and should be unique. You can use it for defending rainbow attacks
- as XOR alone is unbreakable, this algorithm is unbreakable as long there is no attack on the hashing algorithm
- each key is used only once (because of key derivation), private salt multiple times and public salt should be unique
- the block-key depends of the predecessor and the salt

## Roadmap

- Change md5 hashing to a more modern hash or key derivation function like HMAC or HKDF. Each bit should have the same possiblity to be 1 or 0
- more flexible CLI to specify the salt
- Concept how to save the next key
