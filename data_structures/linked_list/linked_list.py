from node import Node as Node


class LinkedList:
    """
    This class is used to assign nodes in a linked list
    """

    def __init__(self, iter=[]):
        """
        this initializes the linked list and creates global variables
        """
        self._current = None
        self.head = None
        self._size = 0
        self.iter = iter

    def reverser(self, data):
        for item in reversed(self.iter):
            self.insert(item)
        return self.iter

    def __repr__(self):
        """
        Used to return head and size of linked list when called
        """
        return '<head> => {}, <_size> => {}'.format(self.head.val, self._size.val)

    def __len__(self):
        """
        returns linked list length when called
        """
        return self._size

    def insert(self, data):
        """
        Inserts a new node into the linked list when called
        """
        self.head = Node(data, self.head)
        self._size += 1
        return self._size

    def find(self, data):
        """
        this test searches for an existing piece of data. coding for this came extensively from the link in resources. See README
        """
        self._current = self.head
        finder = False
        while self._current and finder is False:
            if self._current.get_data() == data:
                finder = True
            else:
                self._current = self._current.get_next()
        if self._current is None:
            raise ValueError("Does not exist")
        return self._current


if __name__=='__main__':

    # Start with the empty list
    ll = LinkedList()
    ll(1)


