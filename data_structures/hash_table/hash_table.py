from hash_linked_list import LinkedList as LL
from node import Node
from functools import reduce


class HashTable:
    def __init__(self, max_size=1024):
        """Initialize a hash_table"""
        self.max_size = max_size
        self.buckets = [None] * self.max_size

    def hash_key(self, key):
        """Generate a hash_key"""
        if type(key) is not str:
            raise TypeError

        # iterate through key and convert each char to ascii char code
        # sum all char codes for a total int value
        # return => mod total by number of buckets

        # # this works
        # sum = 0
        # for char in key:
        #     sum += ord(char)
        # return sum % self.buckets

        # and so does this
        return reduce(lambda a, b: a + ord(b), list(key), 0) % self.buckets

    def set(self):
        """Set a node into the hash table"""
        # hash the key; get a location for the bucket to insert into
        # set val into bucket

        # You will handle collisions here...
        # Your values may look something like a DB record, any of which could be the key:
            # {
            #     'id': '123',
            #     'name': 'xxx',
            #     'title': 'zzz',
            # }
        
        # # this works
        # idx = self.hash_key(key)
        # self.buckets[idx] = val

        # this is refactored version
        self.buckets[self.hash_key(key)] = val

    def get(self):
        """Return a node from a hash_table."""
        return self.buckets[self.hash_key(key)]

    def remove(self):
        """Remove a node from the hash table."""
        temp = self.buckets[self.hash_key(key)]
        self.buckets[self.hash_key(key)] = None
        return temp

