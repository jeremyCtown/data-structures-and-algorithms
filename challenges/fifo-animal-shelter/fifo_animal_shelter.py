from node import Node


class Dog:
    def __init__(self):
        self.val = 'dog'

    # def __repr__(self):
    #     return self.val


class Cat:
    def __init__(self):
        self.val = 'cat'

    # def __repr__(self):
    #     return self.val


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.back = None
        self._size = 0

    def enqueue(self, value):
        """
        creates new node and pushes to queue
        """

        if self.front is None:
            self.front = self.back = Node(value)
            self._size += 1
        else:
            self.back._next = self.back = Node(value)
            self._size += 1
        return self.back

    def dequeue(self, pref):
        """
        This pops the next animal with value of 'pref'
        """

        prev = self.front
        current = self.front._next

        while current:
            import pdb; pdb.set_trace()
            if self.front.val == pref or pref is None:
                self.front = self.front._next
                self._size -= 1
                return prev.val
            elif current.val == pref:
                pet = current
                prev._next = current._next
                self._size -= 1
                return pet
            else:
                prev = current
                current = current._next



