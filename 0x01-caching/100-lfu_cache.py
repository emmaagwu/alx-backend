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
        self.freq_map = {}  # Dictionary to track frequency of each key

    def _update_frequency(self, key):
        """Updates the frequency of the given key and reorders
        the frequency map.
        """
        if key in self.freq_map:
            self.freq_map[key] += 1
        else:
            self.freq_map[key] = 1

        # Reorder items based on updated frequency
        sorted_freq_map = sorted(
            self.freq_map.items(), key=lambda item: item[1]
        )
        self.freq_map = dict(sorted_freq_map)

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
            self._update_frequency(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find and remove the least frequently used item
                lfu_key = next(iter(self.freq_map))
                self.cache_data.pop(lfu_key)
                self.freq_map.pop(lfu_key)
                print("DISCARD:", lfu_key)

            # Add new item and initialize its frequency
            self.cache_data[key] = item
            self.freq_map[key] = 1

    def get(self, key):
        """Retrieves an item by key from the cache.

        Updates the frequency of the accessed item to reflect its
        recent use.
        """
        if key in self.cache_data:
            self._update_frequency(key)
            return self.cache_data[key]
        return None
