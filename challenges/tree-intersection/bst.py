from node import Node


class BST:
    def __init__(self, iter=[]):
        self.root = None
        self.iter = iter

        for item in self.iter:
            self.insert(item)

    def __repr__(self):
        return '<BST Root {}>'.format(self.root.val)

    def __str__(self):
        return self.root.val

    def insert(self, val):
        """Insert a new node into tree."""
        node = Node(val)
        current = self.root

        if self.root is None:
            self.root = node
            return node

        while current:
            if val >= current.val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = node
                    break

            elif val < current.val:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = node
                    break

        return node

    def traverse(self, operation):
        """Operate in_order on nodes."""
        def _walk(node=None):
            if node is None:
                return None

            if node is not None:
                _walk(node.left)
                operation(node)
                _walk(node.right)

        _walk(self.root)

