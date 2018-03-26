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
        # self.head = Node(data, self.head)
        # self._size += 1

        node = Node(data)
        node.next = self.head
        self.head = node
        return self.head

    def reverser(self, data):
        self.iter = reversed(self.iter)
        for item in self.iter:
            self.insert(item)
        return self.iter

    # def find(self, data)
    #     """
    #     Loops through linked list to find if a value exists
    #     """


if __name__=='__main__':

    # Start with the empty list
    ll = LinkedList()
    ll.reverser()


