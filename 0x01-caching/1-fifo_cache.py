#!/usr/bin/env python3
"""fifo caching system"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """fifo caching system"""
    def __init__(self):
        """initializing the class"""
        super().__init__()
        self.key_index = []

    def put(self, key, item):
        """assigning key to item"""
        if item is None or key is None:
            pass
        else:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                item_deleted = self.key_index.pop(0)
                del self.cache_data[item_deleted]
                print("DISCARD:", item_deleted)

            self.cache_data[key] = item
            self.key_index.append(key)

    def get(self, key):
        """gets the key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
