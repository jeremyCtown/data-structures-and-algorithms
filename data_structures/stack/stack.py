from node import Node


class Stack:
    def __init__(self, iterable=[]):
        self.top = None
        self._size = 0

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

        if not self.top:
            raise IndexError('No top')
        else:
            top = self.top
            self.top = self.top._next
            self._size -= 1
            return top.val

    def peek(self):
        """
        Allows the user to see the value of the top node in the stack
        """
        if not self.top:
            raise IndexError('No top')
        else:
            return self.top.val
