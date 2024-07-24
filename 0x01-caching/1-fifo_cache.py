#!/usr/bin/env python3
"""First-In First-Out caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a FIFO
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is not None and item is not None:
            # Check if the key already exists to avoid reordering
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Remove the first inserted item (FIFO order)
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
