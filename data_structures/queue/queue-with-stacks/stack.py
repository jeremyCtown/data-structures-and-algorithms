from node import Node


class Stack:
    def __init__(self, iterable=[]):
        self.top = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        return '<head> => {}'.format(self.top.val)

    def push(self, val):
        """
        creates new node and pushes to stack
        """
        self.top = Node(val, self.top)
        self._size += 1
        return self.top

    def pop(self):
        """
        This pops the top node and assigns the head to the next node
        """

        if self.top is None:
            return None
        else:
            top = self.top
            self.top = self.top._next
            self._size -= 1
            return top

    def peek(self):
        """
        Allows the user to see the value of the top node in the stack
        """
        if self.top is None:
            return None
        else:
            return self.top
