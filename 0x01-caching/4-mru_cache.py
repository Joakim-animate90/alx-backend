#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching
class MRUCache(BaseCaching):
    """
    MRUCache defines a Most Recently Used caching system
    """
    def __init__(self):
        """ Initialize the class
        """
        super().__init__()
        self.order = []
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.order.remove(key)
                self.order.append(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    print("DISCARD: {}".format(self.order[-1]))
                    del self.cache_data[self.order[-1]]
                    self.order.pop(-1)
                self.cache_data[key] = item
                self.order.append(key)
        else:
            pass
    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        else:
            return None