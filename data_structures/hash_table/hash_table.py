from hash_linked_list import LinkedList as LL


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

    def set(self, key, val):
        """Set a node into the hash table."""
        self.buckets[self.hash_key(key)].append({key:val})
        self._size += 1

    def get(self, key, filter=None):
        """Return a node from a hash table."""
        current = self.buckets[self.hash_key(key)].head
        result = []
        while current:
            if key in current.val.keys():
                result.append(current.val[key])
            current = current._next
        return result

    def remove(self, key):
        """Remove value from bucket."""
        bucket = self.buckets[self.hash_key(key)]
        current = bucket.head

        if current is None:
            raise ValueError('Key is not in hash table')

        if key in bucket.head.val.keys():
            deleted = current
            bucket.head = current._next
            current = None
            self._size -= 1
            return deleted

        while current:
            if key in current.val.keys():
                deleted = current
                last._next = current._next
                current = None
                self._size -= 1
                return deleted

            last = current
            current = current._next


        
