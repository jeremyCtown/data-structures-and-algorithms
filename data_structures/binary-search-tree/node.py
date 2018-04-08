class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self):
        return '<Node Val: {}'.format(self.val)

    def __str__(self):
        return self.val
