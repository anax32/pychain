import pychain


def test_create_chain_creates_genesis_block():
    x = pychain.Chain()

    assert x is not None
    assert len(x) == 1


def test_append_item_increase_chain_length():
    x = pychain.Chain()

    assert x is not None
    assert len(x) == 1

    x.append("a")

    assert len(x) == 2
