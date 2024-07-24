#!/usr/bin/env python3
"""lru caching system"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """lru caching system"""
    def __init__(self):
        """initializing the class"""
        super().__init__()
        self.key_index = []

    def put(self, key, item):
        """assigning key to item"""
        if item is None or key is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data:
                print("DISCARD: {}" .format(self.key_index[0]))
                del self.cache_data[self.key_index[0]]
                del self.key_index[0]

            if key in self.key_index:
                del self.key_index[self.key_index.index(key)]

            self.key_index.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """gets the key"""
        if key is not None and key in self.cache_data.keys():
            del self.key_index[self.key_index.index(key)]
            self.key_index.append(key)
            return self.cache_data[key]
        return None
