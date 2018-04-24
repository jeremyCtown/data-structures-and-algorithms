from node import Node

class KTree:

    def __init__(self):
        self._root = Node()

    def __repr__(self):
        return self._root

    def __str__(self):
        return 'Root Val: {}'.format(self._root.val)

    def pre_order(self, operation):
        """
        Operates on nodes starting at the root and 
        moving left, then right
        """
        def _walk(node=None):

            if node is not None:
                operation(node)
                _walk(node.left)
                _walk(node.right)

        _walk(self.root)

    def post_order(self, operation):
        """
        Operates on nodes starting on left side and 
        moving bottom to top, then switching to right side 
        before moving to root
        """
        def _walk(node=None):

            if node is not None:
                _walk(node.left)
                _walk(node.right)
                operation(node)

        _walk(self.root)
    
    
    def insert(self, val, current):
        """
        Inserts a new node into the tree
        """
        current = self._root
        
        if val is None:
            raise ValueError
        
        if current and not current.val:
            temp = None

            for child in current.children:
                if val[0] == child.val:
                    temp = child
                    break

            if temp:
                self.insert(val, temp)
            else:
                newNode = Node(val=val[0])
                current.children.append(newNode)
                self.insert(val, newNode)
        else:
            if len(val) > 1:
                temp = None

                for child in current.children:
                    if val[1] == child.value:
                        tmpChild = child
                        break
                
                if tmpChild:
                    self.insert(val[1:], tmpChild)
                else:
                    newNode = Node(value=val[1])
                    current.children.append(newNode)
                    self.insert(val[1:], newNode)

