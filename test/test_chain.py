import nose
from nose.tools import *

from chain import Chain, SignedChain
from block import Block

class Chain_Tests ():
  def setUp (self):
    self.chain = Chain (Chain.genesis, Chain.hash)

  def test_genesis_function (self):
    L = [[], [], []]


  def test_starts_with_one_block (self):
    assert_equals (1, len (self.chain))

  def test_starts_with_genesis_block (self):
    assert_equals ("GENESIS BLOCK", self.chain.data[0])

  def test_is_valid_chain_one_entry (self):
    assert_true (self.chain.is_valid ())

  def test_add_block (self):
    self.chain.append (bytes ("block 2"))

    assert_equals (2, len (self.chain))
    assert_equals ("block 2", self.chain.data[-1])

  def test_is_valid (self):
    self.chain.append ("block 2")
    self.chain.append ("block 3")
    self.chain.append ("block 4")

    assert_equals (4, len (self.chain))
    assert_true (self.chain.is_valid ())

  def test_get_item (self):
    b = self.chain[0]
    assert_equals (4, len (b))
    assert_true ("data" in b.keys ())
    assert_true ("time" in b.keys ())
    assert_true ("hash" in b.keys ())
    assert_true ("prev" in b.keys ())


class SignedChain_Tests ():
  def setUp (self):
    self.chain = SignedChain (SignedChain.genesis, Chain.hash, "D3AD")

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