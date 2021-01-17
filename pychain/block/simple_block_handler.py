"""
Implementations of block structures
"""
import time


class SimpleBlockHandler:
    """
    Handler for blocks which are represented
    as dictionary objects.
    """

    def __init__(self):
        pass

    def create(self, data):
        """
        creates a dict with the data and time fields set
        hash, and prev will be set in the chain
        """
        return {"data": data, "time": time.time()}

    def read(self, iobuf):
        """
        read block from external source
        """
        pass

    def write(self, iobuf):
        """
        write block to external sink
        """
        pass
