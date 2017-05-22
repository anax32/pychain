import hashlib
import time

class Block:
  def __init__ (self, index, prev_block_hash, timestamp, data):
    self.index = index
    self.previousHash = prev_block_hash
    self.timestamp = timestamp
    self.data = data
    self.hash = Block.hash (str (self))

  def __str__ (self):
    return " ".join ([str (self.index),
                      str (self.previousHash),
                      str (self.timestamp),
                      str (self.data)])

  @classmethod
  def hash (cls, data):
    return hashlib.sha256 (data.encode ('utf-8')).hexdigest ()
