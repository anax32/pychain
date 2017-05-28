# pychain

Basic implementation of a blockchain

+ Chain  
  - hashes data including the hash of previous blocks. 
  - Chain is not a proof-of-work system

+ SignedChain  
  - all block hashes must begin with a given signature; 
  - SignedChain is a proof-of-work blockchain system

# Examples

Compute a blockchain of a few meaningless strings:

```python
import pychain as pyc

c = pyc.SignedChain ("ab")
c.append ("no-one")
c.append ("expects")
c.append ("the spammish")
c.append ("improbabishion")
```

Query some aspects of the chain:

```python
len (c)
c.is_valid ()
genesis_block_data = c[0]["data"]
expects = c[2]["data"]
spammish_hash = c[3]["hash"]
```

Compute a blockchain of image data from pngs (using pypng):

```python
import pychain as pyc
import png

c = pyc.SignedChain ("fa")
c.append (png.Reader ("1.png").read ())
c.append (png.Reader ("2.png").read ())
c.append (png.Reader ("3.png").read ())
```

etc.


# See Also
https://github.com/lhartikk/naivechain

https://medium.com/@lhartikk/a-blockchain-in-200-lines-of-code-963cc1cc0e54
