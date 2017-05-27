import nose
from nose.tools import *

from chain import Chain
from block import Block

class Chain_Tests ():
  def setUp (self):
    self.chain = Chain (Block.genesis)

  def test_starts_with_one_block (self):
    assert_equals (1, len (self.chain.chain))

  def test_get_last_block (self):
    assert_not_equals (None, self.chain.get_last_block ())

  def test_starts_with_genesis_block (self):
    b = self.chain.get_last_block ()
    assert_equals (0, b.index)
    assert_true (isinstance (b, Block))

  def test_is_valid_chain_one_entry (self):
    assert_true (self.chain.is_valid_chain ())

  def test_create_block (self):
    b = self.chain.create_block ("block 2")

    assert_equals (1, b.index)
    assert_equals ("block 2", b.data)

  def test_add_block (self):
    b = self.chain.create_block ("block 2")
    self.chain.add_block (b)

    lb = self.chain.get_last_block ()

    assert_equals (1, lb.index)
    assert_equals ("block 2", lb.data)

  def test_is_valid (self):
    self.chain.add_block (self.chain.create_block ("block 2"))
    self.chain.add_block (self.chain.create_block ("block 3"))
    self.chain.add_block (self.chain.create_block ("block 4"))

    assert_equals (4, len (self.chain.chain))
    assert_true (self.chain.is_valid_chain ())

class TwoChain_Tests ():
  def setUp (self):
    self.A = Chain (Block.genesis)
    self.B = Chain (Block.genesis)

  def test_replace_chain (self):
    self.A.add_block (self.A.create_block ("block 2"))
    self.B.add_block (self.B.create_block ("block 2"))
    self.B.add_block (self.B.create_block ("block 3"))
    assert_true (self.A.replace_chain (self.B))

  def test_replace_chain_fails_on_len (self):
    self.A.add_block (self.A.create_block ("block 2"))
    self.A.add_block (self.A.create_block ("block 3"))
    self.B = Chain (Block.genesis)
    self.B.add_block (self.B.create_block ("block 2"))
    assert_false (self.A.replace_chain (self.B))

  def test_replace_chain_fails_on_equal (self):
    self.A.add_block (self.A.create_block ("block 2"))
    self.A.add_block (self.A.create_block ("block 3"))
    self.B.add_block (self.B.create_block ("block 2"))
    self.B.add_block (self.B.create_block ("block 3"))
    assert_false (self.A.replace_chain (self.B))