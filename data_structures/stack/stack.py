from node import Node


class Stack:
    def __init__(self, iterable=[]):
        self.top = None
        self._current = 0
        # self._size = 0 (optional)

    # We would also define our magics for more info

    def push(self, val):
        """
        creates new node and pushes to stack
        """
        ## these 3 are refactored as one liner just like LLs
        # node = Node(val)
        # node._next = self.top
        # self.top = node

        # this is an example of how to raise an error if wrong input
        if type(val) is not int:
            raise TypeError('Your argument is invalid')

        # better implementation of raising an error
        try:
            self.top = Node(val, self.top)
            self._current += 1
        except TypeError:
            # handle the thing
            pass

        return self.top

    def push_2(self, val):
        """
        This is a refactored version of push above
        """
        try:
            node = Node(val)
        except TypeError:
            pass

        node._next = self.top
        self.top = node

        self._current += 1

        return self.top

    def pop(self):
        try:
            top = self.top
            self.top = self.top._next
            self._current -= 1
            return top
        except AttributeError:
            return None

    def peek(self):
        pass
