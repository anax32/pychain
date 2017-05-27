from chain import Chain

class SignedChain(Chain):
  @staticmethod
  def genesis (chain, hash_function):
    chain.nonce.append (0)
    Chain.genesis (chain, hash_function)

  @staticmethod
  def signed_hash (block_def, sign):
    hash = sign[::-1] + ("0" * (64 - len (sign)))

    try:
      block_def["nonce"]
    except:
      block_def.update ({"nonce": 0})

    while hash.startswith (sign.lower ()) == False:
      block_def["nonce"] += 1
      hash = Chain.hash (block_def)

    return hash

  def __init__ (self, genesis_function, hash_function, sign):
    self.nonce = []
    self.sign = sign.lower ()
    l_hash_fn = lambda x : SignedChain.signed_hash (x, self.sign)
    Chain.__init__ (self, genesis_function, l_hash_fn)

  def __getitem__ (self, i):
    b = Chain.__getitem__ (self, i)
    b.update ({"nonce" : self.nonce[i]})
    return b