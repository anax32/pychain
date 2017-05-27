import nose
from nose.tools import *

from block import SignedBlock
from signed_chain import SignedChain

class SignedChain_Tests:
  def setUp (self):
    self.chain = SignedChain (0xD3AD, SignedBlock.genesis)
    assert_true (isinstance (self.chain, SignedChain))

  def test_starts_with_one_block (self):
    assert_equals (1, len (self.chain.chain))
    assert_true (isinstance (self.chain, SignedChain))

  def test_starts_with_genesis_block (self):
    b = self.chain.get_last_block ()
    assert_equals (0, b.index)    
    assert_true (isinstance (b, SignedBlock))

  def test_create_block (self):
    b = self.chain.create_block ("block 2")
    assert_true (isinstance (self.chain, SignedChain))
    assert_true (isinstance (b, SignedBlock))