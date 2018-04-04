from node import Node


class LinkedList:
    """
    Doc strings are gud
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
        return self.head

    def append(self, val):
        """
        appends node to the end of the LL
        """
        if self.head is None:
            self.insert(val)

        else:
            current = self.head
        while current:
            if current._next is None:
                current._next = Node(val)
                self._size += 1
                return current
            current = current._next

    def insert_before(self, val, new_val):
        """
        inserts node before node at val
        """
        current = self.head
        previous = None
        while current:
            if current.val == val:
                if previous is None:
                    self.insert(new_val)
                    break
                else:
                    new_node = Node(new_val)
                    new_node._next = current
                    previous._next = new_node
                    self.size += 1
                    return new_node
            previous = current
            current = current._next

            if current is None:
                    raise ValueError("Data not in list")

    def insert_after(self, val, new_val):
        """
        inserts node after node at val
        """

        current = self.head
        while current:
            if current.val == val:
                placeholder = current._next
                current._next = Node(new_val)
                current._next._next = placeholder
                self.size += 1
                return current._next

        current = current._next


