import nose
from nose.tools import *

from block import Block, SignedBlock

class SignedBlock_Tests:
  def test_create (self):
    b = SignedBlock (1, 0x1234, 10, "abcd", 2)
    assert_equals (1, b.index)
    assert_equals (0x1234, b.previousHash)
    assert_equals (10, b.timestamp)
    assert_equals ("abcd", b.data)
    assert_equals (2, b.nonce)

  def test_to_string (self):
    b = SignedBlock (1, 0x1234, 10, "abcd", 2)
    assert_equals ("1 4660 10 abcd 2", str (b))

  def test_genesis (self):
    b = SignedBlock.genesis ()
    assert_equals (0, b.index)
    assert_equals ("SIGNED GENESIS BLOCK", b.data)