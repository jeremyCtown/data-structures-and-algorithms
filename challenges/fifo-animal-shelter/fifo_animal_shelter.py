from node import Node


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.back = None
        self._size = 0

    def __repr__(self):
        return 'Next available pet is {self.front.val}'

    def enqueue(self, val):
        """
        creates new node and pushes to queue
        """

        if self.front is None:
            self.back = self.front = Node(val)
            self._size += 1
        else:
            self.back._next = self.back = Node(val)
            self._size += 1
        return self.back

    def dequeue(self, pref):
        """
        This pops the next animal with value of 'pref'
        """

        prev = self.back
        current = self.front

        while current is not None and self._size != 0:
            # import pdb; pdb.set_trace()
            # if current.val == pref.val:
            #     pet = prev.val
            #     self.front = self.front._next
            #     self._size -= 1
            #     return pet
            if current.val.val == pref.val:
                pet = current.val
                prev._next = current._next
                self._size -= 1
                return pet
            else:
                prev = current
                current = current._next

        else:
            raise Exception(('We are all out of {}s').format(pref.val))

