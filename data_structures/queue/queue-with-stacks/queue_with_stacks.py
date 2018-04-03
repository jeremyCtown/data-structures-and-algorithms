from node import Node
from stack import Stack


class Queue:
    def __init__(self):
        self._size = 0
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, val):
        """
        creates new node and pushes to queue
        """
        node = Node(val)

        while len(self.out_stack) != 0:
            self.in_stack.push(self.out_stack.pop())

        self.in_stack.push(node)
        self._size += 1

    def dequeue(self):
        """
        returns front node
        """

        while len(self.in_stack) != 0:
            var = self.in_stack.pop()
            self.out_stack.push(var)

        self.out_stack.pop()
        self._size -= 1



