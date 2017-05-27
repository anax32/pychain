import nose
from nose.tools import *

from chain import Chain
from signed_chain import SignedChain

class Hash_Tests ():
  def test_hash_function (self):
    T = {"nonce" : 0, "A": "A", "B": "B", "C": "C", "D": "D"}
    S = "BEeF"
    exp = "beefba25e6e1ea0c25ab6f4af0dee1e87cf20fdad3b234ca01ccb1034a4b394b"
    h = SignedChain.signed_hash (T, Chain.hash, S)

    assert_true (h.startswith (S.lower ()))
    assert_equals (exp, h)
    assert_equals (3788, T["nonce"])

class Genesis_Block_Tests ():
  def test_genesis_function (self):
    sign = "beef"
    b = SignedChain.genesis (sign)
    assert_equals (5, len (b))
    assert_true ("data" in b)
    assert_true ("nonce" in b)
    assert_true ("hash" in b)

    assert_equals ("GENESIS BLOCK", b["data"])
    assert_true (b["hash"].startswith (sign))

class Function_Tests ():
  def setUp (self):
    self.chain = SignedChain ("D3AD")

  def test_nonce_array_exists (self):
    assert_true (isinstance (self.chain, SignedChain))
    assert_true (len (self.chain.nonce), 1)

  def test_get_item (self):
    b = self.chain[0]
    assert_equals (5, len (b))
    assert_true ("data" in b.keys ())
    assert_true ("time" in b.keys ())
    assert_true ("hash" in b.keys ())
    assert_true ("prev" in b.keys ())
    assert_true ("nonce" in b.keys ())

class Sequence_Tests ():
  def setUp (self):
    self.chain = SignedChain ("b4") # quick
    #self.chain = SignedChain ("b451c") # slow
    #self.chain = SignedChain ("b3426dacdasfa241")  # wtf

  def test_is_valid (self):
    self.chain.append ("block 2")
    self.chain.append ("block 3")
    self.chain.append ("block 4")

    assert_equals (4, len (self.chain))
    assert_true (self.chain.is_valid ())

  def test_is_valid_fails (self):
    self.chain.append ("block 2")
    #fiddle the hash so it doesn't match the sign
    b = self.chain.make ("block 3", self.chain[1]["hash"])
    b["hash"] = "b6" + b["hash"][2:]
    self.chain[2] = b
    self.chain.append ("block 4")

    assert_equals (4, len (self.chain))
    assert_false (self.chain.is_valid ())