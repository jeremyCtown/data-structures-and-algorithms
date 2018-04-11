from queue import Queue
from bst import BST as tree
from node_bst import Node as node


def breadth_first_traversal(tree):
    """
    Prints out bst from top to bottom, left to right
    """
    q = Queue()
    q.enqueue(tree.root)
    test = [] # for testing purposes only

    while q:
        temp = q.front
        out = q.dequeue().val.val
        print(out)
        test.append(out) # for testing purposes only

        if temp.val.left:
            q.enqueue(temp.val.left)
        if temp.val.right:
            q.enqueue(temp.val.right)
    return test