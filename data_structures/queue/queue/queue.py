from node import Node


class Queue:
    def __init__(self, iterable=[]):
        self.front = None
        self.back = None
        self._size = 0

        for item in iterable:
            self.enqueue(item)

    def enqueue(self, val):
        """
        creates new node and pushes to queue
        """

        if self.front is None:
            self.front = self.back = Node(val)
            self._size += 1
        else:
            self.back._next = self.back = Node(val)
            self._size += 1
        return self.back

    def dequeue(self):
        """
        This pops the front node and assigns the front to the next node
        """

        head = self.front

        if self.front is None:
            return None
        elif self.front is self.back:
            self.front = None
            self.back = self.front
            self._size -= 1
        else:
            self.front = self.front._next
            self._size -= 1

        return head

