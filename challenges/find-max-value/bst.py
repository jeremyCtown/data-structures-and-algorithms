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

    def in_order(self, operation):

        def _walk(node=None):
            if node is None:
                return None

            if node is not None:
                _walk(node.left)
                operation(node.val)
                _walk(node.right)

        _walk(self.root)

    def pre_order(self, operation):
        def _walk(node=None):

            if node is not None:
                operation(node)
                _walk(node.left)
                _walk(node.right)

        _walk(self.root)

    def post_order(self, operation):
        def _walk(node=None):

            if node is not None:
                _walk(node.left)
                _walk(node.right)
                operation(node)

        _walk(self.root)
