import hashlib
import time

"""
A block has a hash which is just any old hash of the parameters
"""
class Block:
  @classmethod
  def genesis (cls):
    return Block (0, "0", 0, "GENESIS BLOCK")

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
  def hash (cls, input):
    return hashlib.sha256 (input.encode ("utf-8")).hexdigest ()

"""
A SignedBlock adds the nonce parameter used for proof-of-work systems
NB: The sign is controlled by the chain (the block container)
The nonce parameter is used to control whether the sign is present in the hash
"""
class SignedBlock (Block):
  @classmethod
  def genesis (cls):
    return SignedBlock (0, "0", 0, "SIGNED GENESIS BLOCK", 1)

  def __init__ (self, index, prev_block_hash, timestamp, data, nonce):
    self.nonce = nonce
    Block.__init__ (self, index, prev_block_hash, timestamp, data)

  def __str__ (self):
    return " ".join ([Block.__str__ (self), str (self.nonce)])