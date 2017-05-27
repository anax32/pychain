from block import SignedBlock
from chain import Chain

import time

class SignedChain (Chain):
  def create_block (self, data):
    lb = self.get_last_block ()
    return SignedBlock (lb.index+1, lb.hash, time.time (), data, 0)

  def __init__ (self, key, genesis_function):
    self.key = key
    Chain.__init__ (self, genesis_function)

