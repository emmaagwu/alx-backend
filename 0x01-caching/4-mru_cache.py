#!/usr/bin/env python3
"""Module for Most Recently Used (MRU) caching.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Implements a caching system where the most recently
    used item is discarded when the cache exceeds its limit.
    """
    def __init__(self):
        """Set up the cache with an empty OrderedDict.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Insert or update an item in the cache.

        If the cache exceeds the maximum number of items,
        the most recently used item is removed.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item and move it to the end
            self.cache_data.move_to_end(key, last=True)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(last=True)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item

        # Ensure the newly added or updated item is at the end
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Fetch an item from the cache by key.

        Moves the accessed item to the end to mark it
        as recently used.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)
        return self.cache_data.get(key, None)

