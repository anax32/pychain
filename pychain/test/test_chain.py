import nose
from nose.tools import *

from pychain import Chain

class Hash_Tests ():
  def test_hash_function (self):
    T = {"A":"A", "B":"B", "C":"C", "D":"D"}
    exp = "e12e115acf4552b2568b55e93cbd39394c4ef81c82447fafc997882a02d23677"
    h = Chain.hash (T)
    assert_equals (exp, h)

class Gensis_Block_Tests():
  def test_genesis_function (self):
    b = Chain.genesis ()
    assert_equals (4, len (b))
    assert_true ("data" in b)
    assert_equals ("GENESIS BLOCK", b["data"])

class Function_Tests ():
  def setUp (self):
    self.chain = Chain (Chain.genesis)

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

  def test_get_item (self):
    b = self.chain[0]
    assert_equals (4, len (b))
    assert_true ("data" in b.keys ())
    assert_true ("time" in b.keys ())
    assert_true ("hash" in b.keys ())
    assert_true ("prev" in b.keys ())

class Sequence_Tests ():
  def setUp (self):
    self.chain = Chain (Chain.genesis)

  def test_is_valid (self):
    self.chain.append ("block 2")
    self.chain.append ("block 3")
    self.chain.append ("block 4")

    assert_equals (4, len (self.chain))
    assert_true (self.chain.is_valid ())

  def test_is_valid_fails (self):
    self.chain.append ("block 2")
    self.chain[len (self.chain)] = self.chain.make ("block 3", "3526263")
    self.chain.append ("block 4")

    assert_equals (4, len (self.chain))
    assert_false (self.chain.is_valid ())