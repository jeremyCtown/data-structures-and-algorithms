from node import Node


class LinkedList:
    """
    initializes LL
    """
    def __init__(self, iter=[]):
        self.head = None
        self._size = 0

        for item in reversed(iter):
            self.insert(item)

    def __repr__(self):
        """
        assumes head will have a val and we will need this
        """
        return '<head> => {}'.format(self.head.val)

    def __str__(self):
        """ this is where we can see the list"""

    def __len__(self):
        """
        returns size of LL
        """
        return self._size

    def insert(self, val):
        """
        basic insertion method for adding to front of LL
        """
        self.head = Node(val, self.head)
        self._size += 1

    def append(self, val):
        """
        appends node to the end of the LL
        """
        new_node = Node(val, None)
        current = self.head._next
        while current._next is not None:
            current._next = current._next._next
            if current._next._next is None:
                current._next._next = new_node
                new_node._next is None
                self._size += 1
                return new_node._next

    def insert_before(self, val, new_val):
        """
        inserts node before node at val
        """
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
        """
        inserts node after node at val
        """
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
        """
        returns node at kth from end
        """
        if self._size - k < 0:
            raise AttributeError

        current = self.head
        for i in range(self._size - k - 1):
            current = current._next
        return current

