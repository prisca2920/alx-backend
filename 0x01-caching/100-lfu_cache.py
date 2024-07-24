#!/usr/bin/env python3
""" lfu caching system"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """lfu caching system"""

    def __init__(self):
        """ initializing class """
        self.temp = {}
        super().__init__()

    def put(self, key, item):
        """ Adds an item """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data.keys()) > self.MAX_ITEMS:

                pop = min(self.temp, key=self.temp.get)
                self.temp.pop(pop)
                self.cache_data.pop(pop)
                print(f"DISCARD: {pop}")
            if key not in self.temp:
                self.temp[key] = 0
            else:
                self.temp[key] += 1

    def get(self, key):
        """ Gets an item"""
        if key is None or key not in self.cache_data:
            return None
        self.temp[key] += 1
        return self.cache_data.get(key)
