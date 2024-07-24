#!/usr/bin/env python3
"""Least Frequently Used (LFU) caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class
    """

    def __init__(self):
        """Initialize the class
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.freq_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update item
            self.cache_data[key] = item
            self.freq_data[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Evict least frequently used item
                min_freq = min(self.freq_data.values())
                lfu_keys = \
                    [k for k, v in self.freq_data.items() if v == min_freq]
                lfu_key = lfu_keys[0]
                self.cache_data.pop(lfu_key)
                self.freq_data.pop(lfu_key)
                print("DISCARD:", lfu_key)

            # Add new item
            self.cache_data[key] = item
            self.freq_data[key] = 1

        # Maintain order of cache_data
        self.cache_data.move_to_end(key)

    def get(self, key):
        """Retrieve an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.freq_data[key] += 1
        # Maintain order of cache_data
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
