#!/usr/bin/env python3
"""Least Frequently Used (LFU) Caching System.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Cache system that stores items with LFU eviction policy.

    When the cache reaches its maximum size, the item with the
    least frequency of access is removed.
    """
    def __init__(self):
        """Initializes the LFU cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = OrderedDict()

    def _reorder_items(self, key):
        """Reorders items in the frequency map.
        """
        self.keys_freq[key] += 1
        sorted_items = sorted(
            self.keys_freq.items(), key=lambda item: item[1]
        )
        self.keys_freq = OrderedDict(sorted_items)

    def put(self, key, item):
        """Inserts or updates an item in the cache.

        If the cache exceeds the maximum size, the item with the
        lowest frequency of use is discarded.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update existing item and its frequency
            self.cache_data[key] = item
            self._reorder_items(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find and remove the least frequently used item
                lfu_key = next(iter(self.keys_freq))
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop(lfu_key)
                print("DISCARD:", lfu_key)

            # Add new item and initialize its frequency
            self.cache_data[key] = item
            self.keys_freq[key] = 1
            self._reorder_items(key)

    def get(self, key):
        """Retrieves an item by key from the cache.

        Updates the frequency of the accessed item to reflect its
        recent use.
        """
        if key in self.cache_data:
            self._reorder_items(key)
            return self.cache_data[key]
        return None
