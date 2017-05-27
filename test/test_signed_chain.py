import nose
from nose.tools import *

from chain import Chain
from signed_chain import SignedChain

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