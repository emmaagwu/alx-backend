#!/usr/bin/env python3
"""Module for Least Recently Used (LRU) caching.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Implements an LRU caching system by extending
    the base caching class.
    """
    def __init__(self):
        """Initialize the LRU cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache.

        If the cache exceeds the maximum number of items,
        the least recently used item is discarded.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = next(iter(self.cache_data))
            print("DISCARD:", lru_key)
            self.cache_data.pop(lru_key)

    def get(self, key):
        """Retrieve an item from the cache by key.

        Moves the accessed item to the end to mark it
        as recently used.
        """
        if key is None:
            return None

        item = self.cache_data.get(key)
        if item is not None:
            self.cache_data.move_to_end(key)
        return item
