from ../queue/queue import Queue

from node import Node

class KTree:

    def __init__(self):
        self.root = Node()

    def __repr__(self):
        return self.root

    def __str__(self):
        return 'Root Val: {}'.format(self.root.val)

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

    def breadth_first_traversal(self, operation):
        """
        Performs operation on ktree from top to bottom, left to right
        """
        q = Queue()
        q.enqueue(self.root)
        test = [] # for testing purposes only

        while q:
            temp = q.front
            out = q.dequeue().val.val
            operation(out)
            test.append(out) # for testing purposes only

            if temp.val.left:
                q.enqueue(temp.val.left)
            if temp.val.right:
                q.enqueue(temp.val.right)
        return test
        
    
    def insert(self, parent_val, val):
        """
        Inserts a new node into the tree
        """
        node = Node(val)

        if self.root is None:
            self.root = node
            return

        if parent_val is None:
            self.root.add_child(node)
        
        if current and not current.val:
            temp = None
"""
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

