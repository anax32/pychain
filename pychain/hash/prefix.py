"""
Search for the hash of an object with a given prefix.

This object will add a "nonce" key-value pair to the dictionary.
This key-value pair is required to recreate the hash value of the
dictionary providing no other values change.
"""
from .simple import SimpleHash


class PrefixHash(SimpleHash):
  """
  computes the hash of a dictionary which starts with a given sequence
  """
  def __init__(self, *args, prefix = None, **kwargs):
    super().__init__(*args, **kwargs)

    self.prefix = "" if prefix is None else prefix

  def __call__(self, D):
    """
    compute the hash of D

    if D has a key "nonce", that value will be used as the start point
    of the search.

    NB: integers will not overflow in python, so this function will
    continue searching ever larger numbers. The nonce may be difficult
    to serialise.
    """
    if "nonce" not in D:
      D["nonce"] = 0

    while True:
      c = super().__call__(D)

      if c[:len(self.prefix)] == self.prefix:
        break

      D["nonce"] += 1

    return c
