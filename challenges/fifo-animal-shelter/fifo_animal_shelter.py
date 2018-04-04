from node import Node


class AnimalShelter:
    def __init__(self, val):
        self.front = None
        self.back = None
        self._size = 0

    def enqueue(self, val):
        """
        creates new node and pushes to queue
        """

        if val != 'dog' or val != 'cat':
            return 'Sorry, cats and dogs only'

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

        if pref

        for i in self._size:
            if self.front.val == pref or pref is None:
                new_pet = self.front
                self.front = self.front._next
                self._size -= 1
                return new_pet
            elif current == pref:
                prev._next = current._next
                self._size -= 1
                return current
            else:
                prev = current
                current = current._next




