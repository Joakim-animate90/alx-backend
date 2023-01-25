#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching
class FIFOCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system
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
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    print("DISCARD: {}".format(self.order[0]))
                    del self.cache_data[self.order[0]]
                    self.order.pop(0)
                self.cache_data[key] = item
                self.order.append(key)
        else:
            pass
    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None           