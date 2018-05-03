from hash_linked_list import LinkedList as LL
# from node import Node
from functools import reduce


class HashTable:
    """This is a hash table."""

    def __init__(self, max_size=1024):
        """Initialize a hash_table."""
        self.max_size = max_size
        self.buckets = [LL() for _ in range(self.max_size)]
        self._size = 0

    def hash_key(self, key):
        """Generate a hash_key."""
        if type(key) is not str:
            raise TypeError

        sum = 0
        for char in key:
            sum += ord(char)
        return sum % len(self.buckets)

        # this also works
        # return reduce(lambda a, b: a + ord(b), list(key), 0) % self.buckets

    def set(self, key, val):
        """Set a node into the hash table."""
        self.buckets[self.hash_key(key)].insert({key:val})
        self._size += 1

    def get(self, key, filter=None):
        """Return a node from a hash table."""
        current = self.buckets[self.hash_key(key)].head
        while current:
            if key in current.val.keys():
                return current.val[key]
            current = current._next

    def remove(self, key):
        """Remove value from bucket."""
        remove = self.buckets[self.hash_key(key)]

        current = remove.head
        last = current

        if key in current.val.keys():
            deleted = current
            current = current._next
            self._size -= 1
            return deleted

        while current:
            if key in current.val.keys():
                deleted = current
                current = current._next
                last._next = current
                self._size -= 1
                return deleted
            else:
                last = current
                current = current._next

        
