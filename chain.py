import time
import hashlib

class Chain:
  @staticmethod
  def genesis (chain, hash_function):
    """creates an initial entry in the block chain"""
    chain.data.append ("GENESIS BLOCK")
    chain.time.append (time.time ())
    chain.chsh.append (hash_function ({"data":chain.data[-1], "timestamp":chain.time[-1]}))
    chain.phsh.append (0)

  @staticmethod
  def hash (block_def):
    """computes the hash of block_def.
    Each item in block_def is converted to bytes.
    block_def is a dictionary.
    keys are sorted before hashing, order is ascending key value"""
    h = hashlib.sha256 ()

    for i in sorted (block_def.keys ()):
      h.update (bytes (block_def[i]))

    return h.hexdigest ()

  def __init__ (self, genesis_function, hash_function):
    """creates empty lists for the data, timestampes,
    hash and previous hash.
    Previous hash is stored to avoid recomputing the hash of
    a block to confirm hashs are correct"""
    self.data = []  # data in block
    self.time = []  # time stamp of block
    self.chsh = []  # hash of block
    self.phsh = []  # hash of prev block

    self.hash_fn = hash_function  # hash function
    genesis_function (self, hash_function) # init the chain with a gensis block

  def __len__ (self):
    """returns the number of blocks in the chain"""
    return len (self.chsh)

  def append (self, data):
    """appends a block of data to the chain.
    FIXME: do not use time directly as the timestamp, but give a relative
    offset to the previous block age"""
    self.data.append (data)
    self.time.append (time.time ())
    self.chsh.append (self.hash_fn ({"data": self.data[-1], "timestamp": self.time[-1], "hash": self.chsh[-1]}))

  def is_valid (self):
    """checks hashes and previous hashes match for each block in the chain"""
    for h, p in zip (self.phsh[1:], self.chsh):
      if h != p:
        print (str (h) + " != " + str (p))
        return False
    return True

  def __getitem__ (self, i):
    return {"data" : self.data[i],
            "time" : self.time[i],
            "hash" : self.chsh[i],
            "prev" : self.phsh[i]}

