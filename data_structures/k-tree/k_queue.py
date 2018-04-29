
class Node:
    def __init__(self, val, next=None):
        """Initialize node."""
        self.val = val
        self._next = next

    def __repr__(self):
        """Represent val of node"""
        return self.val

class Queue:
    def __init__(self, val=None):
        """Initialize queue."""
        self.front = None
        self.back = None
        self._size = 0

        # self.enqueue(val)

    def __repr__(self):
        """Represent front of queue."""
        return '<front> => {}'.format(self.front.val)

    def __len__(self):
        """Represent length of queue."""
        return self._size

    def enqueue(self, val):
        """Create new node and pushes to queue."""
        node = Node(val)
        if self.front is None:
            self.front = node
            self.back = node
            self._size += 1
            # import pdb; pdb.set_trace()
        else:
            self.back._next = node
            self.back = node
            self._size += 1
        return self.back

    def dequeue(self):
        """Pop front node and assign front to next node."""

        if not self.front:
            raise IndexError('No front')
        elif self.front is self.back:
            head = self.front
            self.front = None
            self.back = self.front
            self._size -= 1
            return head.val
        else:
            head = self.front
            self.front = self.front._next
            self._size -= 1
            return head.val
        # import pdb; pdb.set_trace()

        

