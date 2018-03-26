import node as Node

class LinkedList:
    """
    This class is used to assign nodes in a linked list
    """

    def __init__(self):
        """
        this initializes the linked list and creates global variables
        """
        self._current = None
        self.head = None
        self._size = 0

    def __repr__(self):
        """
        Used to return size of linked list when called
        """
        return '<head> => {}'.format(self._size.val)

    def __len__(self):
        return self._size

    def insert(self, val):
        self.head = Node(val, self.head)
        self._size += 1
