from k_queue import Queue

from node import Node

class KTree:
    """
    Create a new KTree.
    """

    def __init__(self, val=None):
        """Initialize KTree"""
        self.root = None
        self._size = 0

    def __repr__(self):
        """Magic repr."""
        return 'Root Val: {}'.format(self.root.val)

    def __str__(self):
        """Magic str."""
        return 'Root Val: {}'.format(self.root.val)

    def pre_order(self, operation):
        """
        Operate on nodes starting at the root 
        and moving left, then right.
        """
        def _walk(node=None):
            if node is None:
                return

            operation(node)
            
            for child in node.children:
                _walk(child)

        _walk(self.root)

    def post_order(self, operation):
        """
        Operate on nodes starting on left side and 
        moving bottom to top, then switching to right side 
        before moving to root.
        """
        def _walk(node=None):
            if node is None:
                return

            for child in node.children:
                _walk(child)
            
            operation(node)

        _walk(self.root)

    def breadth_first_traversal(self, operation):
        """
        Perform operation on ktree from top to bottom, left to right.
        """
        q = Queue()
        order = [] # purposed for testing
        q.enqueue(self.root)

        while q:
            temp = q.front
            out = q.dequeue().val.val
            operation(out)
            order.append(out) # purposed for testing

            if temp.val.left:
                q.enqueue(temp.val.left)
            if temp.val.right:
                q.enqueue(temp.val.right)
        return order # purposed for testing
        
    
    def insert(self, val=None, parent_val=None):
        """Insert a new node into the KTree."""
        node = Node(val)
        q = Queue()
        touched = [] #  purposed for testing

        if self.root is None:
            self.root = node
            # import pdb; pdb.set_trace()            

            self._size += 1
            return self.root

        if parent_val is None:
            self.root.add_child(node)
            return

        q.enqueue(self.root)
        while len(q) > 0:
            current = q.dequeue()
            if current.val == parent_val:
                current.add_child(node)
                self._size += 1
                return
            touched.append(current.val) # purposed for testing
            for child in current.children:
                q.enqueue(child)
        return touched # purposed for testing
        
        if current and not current.val:
            temp = None


