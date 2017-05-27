from chain import Chain

class SignedChain(Chain):
  @staticmethod
  def genesis (sign):
    b = Chain.genesis ()
    b.update ({"nonce" : 0})
    b.update ({"hash" : SignedChain.signed_hash (b, Chain.hash, sign)})
    return b

  @staticmethod
  def signed_hash (block_def, hash_fn, sign):
    hash = sign[::-1] + ("0" * (64 - len (sign)))

    while hash.startswith (sign.lower ()) == False:
      block_def["nonce"] += 1
      hash = hash_fn (block_def)

    return hash

  def __init__ (self, sign):
    self.sign = sign.lower ()
    l_genesis_fn = lambda : SignedChain.genesis (self.sign)

    self.nonce = []
    Chain.__init__ (self, l_genesis_fn)

  def __getitem__ (self, i):
    """get the block at index i"""
    b = Chain.__getitem__ (self, i)
    b.update ({"nonce" : self.nonce[i]})
    return b

  def __setitem__ (self, i, value):
    """set the block values at index i, iff i >= len (self)"""
    Chain.__setitem__ (self, i, value)
    self.nonce.append (value["nonce"])

  def make (self, data, previous_hash):
    """create a block dictionary using the super class
    add a nonce field
    produce a new hash"""
    b = Chain.make (self, data, previous_hash)
    b.update ({"nonce" : 0})
    b.update ({"hash" : SignedChain.signed_hash (b, Chain.hash, self.sign)})
    return b

  def is_valid (self):
    """checks the super class validity holds and
    all hashes start with the sign for this chain"""
    return Chain.is_valid (self) and all ([h.startswith (self.sign) for h in self.chsh])