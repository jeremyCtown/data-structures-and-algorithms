
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self._next = next

    def __repr__(self):
        return '{val}'.format(val=self.val)
