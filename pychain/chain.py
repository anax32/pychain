"""
Basic blockchain data-structure

A block is a dictionary object:
```
{
  "data": <some byte sequence>,
  "time": <timestamp>,
  "prev": <previous block hash>
}
```

a blockchain is a sequence of blocks such that
the hash value of the previous block is used in
the definition of the current block hash,

in pseudocode:

```
block(n+1)["prev"] = hash(block(n))
```
"""

import time
import hashlib
import logging


from .genesis_blocks import default_genesis_fn
from .hashers import SimpleHash


logger = logging.getLogger(__name__)


class Chain():
  """
  Chain class creates and manages a blockchain data structure
  in memory

  constructor parameters:
    genesis_fn: the function which creates the genesis block
    hash_fn: function to compute the block hash (any hashlib function will work)

  """
  def __init__ (self, genesis_fn = None, hash_fn = None):
    """
    creates empty lists for the data, timestamps,
    hash and previous hash.
    Previous hash is stored to avoid recomputing the hash of
    a block to confirm hashs are correct
    """
    self.blocks = []

    if genesis_fn is None:
      self.genesis_fn = default_genesis_fn if genesis_fn is None else genesis_fn
    else:
      self.genesis_fn = genesis_fn

    if hash_fn is None:
      self.hash_fn = SimpleHash(ignore_keys=["hash"])
    else:
      self.hash_fn = hash_fn

    # get a genesis block
    g = self.genesis_fn()
    g["hash"] = self.hash_fn(g)
    self.blocks.append(g)


  def __len__ (self):
    """
    return length of the chain
    """
    return len(self.blocks)


  def append(self, data):
    """
    create a block containing data and append to the chain
    """
    block = {
      "data": data,
      "time": time.time(),
      "prev": self.blocks[-1]["hash"]
    }
    block["hash"] = self.hash_fn(block)
    self.blocks.append(block)


  def validate(self):
    """
    validate all the blocks in a chain object
    """
    p_hash = self.hash_fn(self.genesis_fn())

    for idx, block in enumerate(self.blocks[1:]):
      b_hash = self.hash_fn(block)

      logger.info("block[%i]: [%s] %s" % (idx, block["prev"], block["hash"]))

      if block["prev"] != p_hash:
        logger.error("block.prev != hash (%s != %s)" % (str(block["prev"]), str(p_hash)))
        raise Exception()

      if block["hash"] != b_hash:
        logger.error("block.hash != hash (%s != %s)" % (str(block["hash"]), str(b_hash)))
        raise Exception()

      p_hash = b_hash
