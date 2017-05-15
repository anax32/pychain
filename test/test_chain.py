import nose
from nose.tools import *

from chain import Chain

def test_chain_genesis_block ():
  b = Chain.get_genesis_block ()
  assert_equals (0, b.index)
  assert_equals ("GENESIS BLOCK", b.data)

def test_chain_starts_with_one_block ():
  c = Chain ()
  assert_equals (1, len (c.chain))

def test_chain_get_last_block ():
  c = Chain ()
  assert_not_equals (None, c.get_last_block ())

def test_chain_starts_with_genesis_block ():
  c = Chain ()
  b = c.get_last_block ()
  assert_equals (0, b.index)

def test_chain_is_valid_chain_one_entry ():
  c = Chain ()
  assert_true (c.is_valid_chain ())

def test_chain_create_block ():
  c = Chain ()
  b = c.create_block ("block 2")

  assert_equals (1, b.index)
  assert_equals ("block 2", b.data)

def test_chain_add_block ():
  c = Chain ()
  b = c.create_block ("block 2")
  c.add_block (b)

  lb = c.get_last_block ()

  assert_equals (1, lb.index)
  assert_equals ("block 2", lb.data)

def test_chain_is_valid ():
  c = Chain ()
  c.add_block (c.create_block ("block 2"))
  c.add_block (c.create_block ("block 3"))
  c.add_block (c.create_block ("block 4"))

  assert_equals (4, len (c.chain))
  assert_true (c.is_valid_chain ())
