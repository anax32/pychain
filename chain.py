from block import Block

import time

class Chain:
  @classmethod
  def get_genesis_block (cls):
    return Block (0, "0", 0, "GENESIS BLOCK")

  def __init__ (self):
    # genesis
    self.chain = []
    self.chain.append (Chain.get_genesis_block ())

  def get_last_block (self):
    return self.chain[len (self.chain)-1]

  def is_valid_next_block (self, new_block, prev_block):
    if prev_block.index + 1 != new_block.index:
      return False
    if prev_block.hash != new_block.previousHash:
      return False
    if Block.hash (str (new_block)) != new_block.hash:
      return False

    return True

  def add_block (self, new_block):
    if self.is_valid_next_block (new_block, self.get_last_block ()) == False:
      return False

    self.chain.append (new_block)
    return True

  def create_block (self, data):
    lb = self.get_last_block ()
    return Block (lb.index+1, lb.hash, time.time (), data)

  def is_valid_chain (self):
    head = self.chain[0]

    for i in range (1, len (self.chain)):
      if self.is_valid_next_block (self.chain[i], self.chain[i-1]) == False:
        return False

    return True

  def replace_chain (self, other):
    if other.is_valid_chain () == False:
      return False

    if len (other.chain) <= len (self.chain):
      return False

    self.chain = other.chain
    return True