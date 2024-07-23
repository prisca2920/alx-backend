#!/usr/bin/env python3
"""creating a basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """creating a basic caching class"""
    def __init__(self):
        """initializing the class"""
        super().__init__()

    def put(self, key, item):
        """assigning the key and item"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """returns the key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
