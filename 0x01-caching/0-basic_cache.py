#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching
class BasicCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs
    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """

    def __init__(self):
        """ Initialize the class
        """

        super().__init__()

    def put(self, key, item):
        """ Store a key-value pair
        """

        if key is not None and item is not None:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """Must return the value in self.cache_data linked to key.
        """
            
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
