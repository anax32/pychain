"""
functions for creating genesis blocks
"""

import time


def default_genesis_fn():
    """
    creates an initial entry for the block chain
    """
    return {"data": "GENESIS BLOCK", "time": time.time(), "prev": 0}
