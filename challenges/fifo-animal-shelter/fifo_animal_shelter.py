from node import Node


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.back = None
        self._size = 0

    def enqueue(self, val):
        """
        creates new node and pushes to queue
        """

        # if val != 'dog' or val != 'cat':
        #     return 'Sorry, cats and dogs only'

        if self.front is None:
            self.front = self.back = Node(val)
            self._size += 1
        else:
            self.back._next = self.back = Node(val)
            self._size += 1
        return self.back

    def dequeue(self, pref):
        """
        This pops the next animal with value of 'pref'
        """

        prev = self.front
        current = self.front._next

        while current:
            if self.front.val == pref or pref is None:
                self.front = self.front._next
                self._size -= 1
                return pref
            elif current.val == pref:
                prev._next = current._next
                self._size -= 1
                return pref
            else:
                prev = current
                current = current._next



