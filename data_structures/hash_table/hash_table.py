from hash_linked_list import LinkedList as LL
from node import Node
from functools import reduce


class HashTable:
    def __init__(self, max_size=1024):
        """Initialize a hash_table."""
        self.max_size = max_size
        self.buckets = [LL() for _ in range(self.max_size)]

    def hash_key(self, key):
        """Generate a hash_key."""
        if type(key) is not str:
            raise TypeError

        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.buckets

        # this also works
        # return reduce(lambda a, b: a + ord(b), list(key), 0) % self.buckets

    def set(self, key, val):
        """Set a node into the hash table."""
        return self.buckets[self.hash_key(key)].insert({key:val})


    def get(self, key, filter=None):
        """Return a node from a hash table."""
        return self.buckets[self.hash_key(key)]

    def remove(self, key):
        """Remove a node from the hash table."""
        temp = self.buckets[self.hash_key(key)]
        self.buckets[self.hash_key(key)] = None
        return temp

