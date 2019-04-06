# Concept

```python
def encrypt(message, key, difficulty=2):
  for block in message:
    newKey = hash(key)
    encrypted += block ^ newKey[::difficulty]
    key = newKey
```