class LinkedList:
"""
Doc strings are gud
"""
    def __init__(self, iter=[]):
        self.head = None
        self._size = 0
        self._current = self.head

        for item in reversed(iter):
            self.insert(item)

    def __repr__(self):
        """Return value of head."""
        return '<head> => {}'.format(self.head.val)

    def __len__(self):
        """Return size of LL."""
        return self._size

    def insert(self, val):
        """Insert node at head of LL."""
        self.head = Node(val, self.head)
        self._size += 1

    def append(self, val):
        """Append node to the end of the LL."""
        new_node = Node(val, None)
        current = self.head._next
        while current._next is not None:
            current._next = current._next._next
            if current._next._next is None:
                current._next._next = new_node
                new_node._next is None
                self._size += 1
                return new_node._next

    def find(self, val):
        """Search through a list for val and return node with that val."""

        current = self.head
        while current:
            if val == current.val:
                return True

            current = current._next
        return False

    def insert_before(self, val, new_val):
        """Insert node before node at val."""
        new_node = Node(new_val)
        current = self.head._next
        while current._next is not None:
            if current._next.val == val:
                new_node._next = current._next
                current._next = new_node
                self._size += 1
                break

            current = current._next

        if current._next is None:
            raise ValueError("Data not in list")

    def insert_after(self, val, new_val):
        """Inserts node after node at val."""
        new_node = Node(new_val)
        current = self.head._next
        while current._next is not None:
            if current.val == val:
                new_node._next = current._next._next
                current._next = new_node
                self._size += 1
                break

            current = current._next

        if current._next is None:
            raise ValueError("Data not in list")

    def kth_from_end(self, k):
        """Returns node at kth from end."""
        current = self.head
        counter = 0
        answer = 0
        kth = self._size - k
        while current._next is not None:
            if counter == kth:
                answer = current
                break
            else:
                counter += 1
                current = current._next
        return answer