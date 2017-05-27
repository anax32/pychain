import nose
from nose.tools import *

from block import Block

class Block_Tests:
  def test_create (self):
    b = Block (1, 0x1234, 10, "abcd")
    assert_equals (1, b.index)
    assert_equals (0x1234, b.previousHash)
    assert_equals (10, b.timestamp)
    assert_equals ("abcd", b.data)

  def test_to_string (self):
    b = Block (1, 0x1234, 10, "abcd")
    assert_equals ("1 4660 10 abcd", str (b))

  def test_generate_hash (self):
    h = Block.hash ("deadbeef")
    assert_equals ("2baf1f40105d9501fe319a8ec463fdf4325a2a5df445adf3f572f626253678c9", h)

  def test_genesis (self):
    b = Block.genesis ()
    assert_equals (0, b.index)
    assert_equals ("GENESIS BLOCK", b.data)