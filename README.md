# pychain

Basic implementation of a blockchain

+ Chain  
  - hashes data including the hash of previous blocks. 
  - Chain is not a proof-of-work system

+ SignedChain  
  - all block hashes must begin with a given signature; 
  - SignedChain is a proof-of-work blockchain system

## Usage

Compute a blockchain of a few meaningless strings:

```python
>>> import pychain
>>>
>>> ch = pychain.Chain()
>>>
>>> ch.blocks
[{'data': 'GENESIS BLOCK', 'time': 1610876665.9579897, 'prev': 0, 'hash': '0c246fd7378a003fe6ae5a3c3162066578fca3b86c596a72c6d8ee5e62eab505'}]
>>>
>>>
>>> ch.append("1")
>>> ch.append("2")
>>> ch.append("3")
>>>
>>>
>>> ch.blocks
[{'data': 'GENESIS BLOCK', 'time': 1610876665.9579897, 'prev': 0, 'hash': '0c246fd7378a003fe6ae5a3c3162066578fca3b86c596a72c6d8ee5e62eab505'}, {'data': '1', 'time': 1610876681.3811243, 'prev': '0c246fd7378a003fe6ae5a3c3162066578fca3b86c596a72c6d8ee5e62eab505', 'hash': '955ae6da58e1ccbf4486ac85f34a24aa85e6fc77fb061e3812b17fc12b9b3274'}, {'data': '2', 'time': 1610876686.380796, 'prev': '955ae6da58e1ccbf4486ac85f34a24aa85e6fc77fb061e3812b17fc12b9b3274', 'hash': '428152bfa97e1089f47fd4947f43a9d5af1783bb5271ea4df826a36689fc780f'}, {'data': '3', 'time': 1610876688.452741, 'prev': '428152bfa97e1089f47fd4947f43a9d5af1783bb5271ea4df826a36689fc780f', 'hash': 'ffc79b1cb8d6a8ae67a15ffb9bcb8a5610bd803a68d6274dd77a7c1654cd4bc6'}]
>>>
>>>
>>> [b["hash"] for b in ch.blocks]
['0c246fd7378a003fe6ae5a3c3162066578fca3b86c596a72c6d8ee5e62eab505', '955ae6da58e1ccbf4486ac85f34a24aa85e6fc77fb061e3812b17fc12b9b3274', '428152bfa97e1089f47fd4947f43a9d5af1783bb5271ea4df826a36689fc780f', 'ffc79b1cb8d6a8ae67a15ffb9bcb8a5610bd803a68d6274dd77a7c1654cd4bc6']
>>>
>>>
>>> [b["prev"] for b in ch.blocks]
[0, '0c246fd7378a003fe6ae5a3c3162066578fca3b86c596a72c6d8ee5e62eab505', '955ae6da58e1ccbf4486ac85f34a24aa85e6fc77fb061e3812b17fc12b9b3274', '428152bfa97e1089f47fd4947f43a9d5af1783bb5271ea4df826a36689fc780f']
>>>
>>> len(ch)
4
>>>
>>>
```

### Changing the hash function
The `Chain` class takes a `hash_fn` parameter in the constructor to allow a custom hash function.
The default hasher is `pychain.SimpleHash` which uses `hashlib.sha256` under the hood.
We can change `SimpleHash` to use any hash function with a `hashlib` compatabile interface.
For example, to use `hashlib.md5`:
```python
>>> import pychain, hashlib
>>>
>>> md5hasher = pychain.SimpleHash(hash_fn=hashlib.md5)
>>>
>>> ch = pychain.Chain(hash_fn=md5hasher)
>>>
>>> 
>>> ch.blocks
[{'data': 'GENESIS BLOCK', 'time': 1610878768.7230575, 'prev': 0, 'hash': 'bbb9e828a8898b718cfcbc1764b3a61b'}]
>>>
>>>
>>> ch.append("1")
>>> ch.append("2")
>>> ch.append("3")
>>>
>>> [b["hash"] for b in ch.blocks]
['bbb9e828a8898b718cfcbc1764b3a61b', 'ec5436a4aa78825dd96c8dec83db459d', 'fe6d03801168fc4b9a3b74650a44341e', '244e03650a8f763ecf0e61df093347c3']
>>>
>>>
```

### Proof-of-work
A proof-of-work system can be implemented using the `pychain.PrefixHash` object as the block chain hasher:
```python
>>> import pychain
>>> 
>>> 
>>> ch = pychain.Chain(hash_fn=pychain.PrefixHash(prefix="aaaa"))
>>> 
>>> ch.blocks
[{'data': 'GENESIS BLOCK', 'time': 1610878406.9918442, 'prev': 0, 'nonce': 37956, 'hash': 'aaaa2a4c6e5f6974d96323c5276b58162fd721bf0d953af09f8f3f24e618cf72'}]
>>> 
>>> 
>>> ch.append("1")
>>> ch.append("2")
>>> ch.append("3")
>>> 
>>> 
>>> [b["hash"] for b in ch.blocks]
['aaaa2a4c6e5f6974d96323c5276b58162fd721bf0d953af09f8f3f24e618cf72', 'aaaac63baa0f619880f97488f1b9e0681067d1da5a7e527e7f712ac08e8abd26', 'aaaa5ef8105557a3d6dc5ab36f2a18a7facb05483df38947796494e79d0df3a0', 'aaaa126d3b2bab0c0a3c3adeace4479520cf7993afdafd2304b937a3e83d7dd0']
>>> 
>>> 
>>> [b["prev"] for b in ch.blocks]
[0, 'aaaa2a4c6e5f6974d96323c5276b58162fd721bf0d953af09f8f3f24e618cf72', 'aaaac63baa0f619880f97488f1b9e0681067d1da5a7e527e7f712ac08e8abd26', 'aaaa5ef8105557a3d6dc5ab36f2a18a7facb05483df38947796494e79d0df3a0']
>>> 
>>> 
``` 

# Adding files to a blockchain example
Compute a blockchain of data from pngs:

```python
>>> import pychain
>>> 
>>> 
>>> ch = pychain.Chain()
>>> 
>>> 
>>> ch.append(open("1.png", "rb").read())
>>> ch.append(open("2.png", "rb").read())
>>> ch.append(open("3.png", "rb").read())
>>> 
>>> 
>>> [b["hash"] for b in ch.blocks]
['c8c19a3fab9e7287f24a294dacb0ec59ec22b478f50f785e484fdcd0eeb9d299', '504cfa66fc341b2151f922c0f0407f3f455fddde55543e7adad02b23f50e825d', '2afe7441b0f6c4a918566bb6fc7db5ac0191d1ed16400d724a728051f777ab0a', '69ac6b9d4cefe67846317ce813f0dbb2d18e7a325eedfa2268cb36be305ce47b']
>>> 
>>> 
>>> 
```

# See Also
https://github.com/lhartikk/naivechain

https://medium.com/@lhartikk/a-blockchain-in-200-lines-of-code-963cc1cc0e54
