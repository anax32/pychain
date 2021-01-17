"""
block hashing functions
"""
import time
import hashlib
import logging
import struct

from .type_convert import type_to_bytearray


class SimpleHash:
    """
    computes the hash of an in-memory dictionary object.
    Each item in is converted to bytes.
    keys are sorted before hashing, order is ascending key value.

    ignore_keys: list of keys to ignore in the hash

    e.g.:
      default_hash_fn({"test": "a", "ignore-me": "b"}, ["ignore-me"]})
      will produce a hash of the value bytes("a") by ignoring
      the other value in the dict
    """

    def __init__(self, hash_fn=None, ignore_keys=None):
        """
        hash_fn: object which produces a hash of byte arrays. Must have the
                 same interface has the hashlib functions.
                 default is hashlib.sha256
        ignore_keys: list of key names to ignore when computing the hash
        """
        self.ignore_keys = [] if ignore_keys is None else ignore_keys

        if hash_fn is None:
            self.hash_fn = hashlib.sha256
        else:
            self.hash_fn = hash_fn

    def __call__(self, D):
        """
        compute the hash for a dictionary
        """
        hash_keys = [k for k in D.keys() if k not in self.ignore_keys]

        h = self.hash_fn()

        for key in sorted(hash_keys):
            # convert the value to a bytearray
            b = type_to_bytearray(D[key])

            try:
                h.update(b)
            except TypeError:
                logger.error(
                    "could not hash: '%s': [%s]'%s'"
                    % (key, str(type(D[key])), str(D[key]))
                )

        return h.hexdigest()
