#!/usr/bin/env python3
"""Last-In First-Out caching mechanism.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Implements a caching system with a LIFO
    removal policy when the limit is exceeded.
    """
    def __init__(self):
        """Initialize the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not\
                in self.cache_data:
            last_key = next(reversed(self.cache_data))
            self.cache_data.pop(last_key)
            print("DISCARD:", last_key)

        self.cache_data[key] = item
        # Move the added key to the end to maintain LIFO order
        self.cache_data.move_to_end(key)

    def get(self, key):
        """Retrieve an item by key.
        """
        return self.cache_data.get(key)
