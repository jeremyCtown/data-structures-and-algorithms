from queue import Queue
from bst import BST as tree
from node_bst import Node as node

def breadth_first_traversal(tree):
    """

    """
    q = Queue()
    q.enqueue(tree.root)

    while q:
        n = q.front
        import pdb; pdb.set_trace()
        if n.val.left:
            q.enqueue(n.left)
        if n.val.right:
            q.enqueue(n.right)
        print q.dequeue().val