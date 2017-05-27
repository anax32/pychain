import time
import hashlib

class Chain:
  @staticmethod
  def genesis ():
    """creates an initial entry for the block chain"""
    b = {"data" : "GENESIS BLOCK",
         "time" : time.time (),
         "prev" : 0}
    b.update ({"hash" : Chain.hash (b)})
    return b

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

  def __init__ (self, genesis_function):
    """creates empty lists for the data, timestampes,
    hash and previous hash.
    Previous hash is stored to avoid recomputing the hash of
    a block to confirm hashs are correct"""
    self.data = []  # data in block
    self.time = []  # time stamp of block
    self.chsh = []  # hash of block
    self.phsh = []  # hash of prev block

    # get a genesis block
    self.__setitem__ (0, genesis_function ())

  def __len__ (self):
    """returns the number of blocks in the chain"""
    return len (self.chsh)

  def make (self, data, previous_hash):
    """creates a block out of thin air
    FIXME: do not use time directly as the timestamp, but give a relative
    offset to the previous block age"""
    b = {"data" : data,
         "time" : time.time (),
         "prev" : previous_hash}
    b.update ({"hash" : Chain.hash (b)})
    return b
    
  def append (self, data):
    """appends a block of data to the chain."""
    self.__setitem__ (len (self), self.make (data, self.chsh[-1]))

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

  def __setitem__ (self, i, value):
    if i >= len (self):
      self.data.append (value["data"])
      self.time.append (value["time"])
      self.chsh.append (value["hash"])
      self.phsh.append (value["prev"])
    else:
      raise