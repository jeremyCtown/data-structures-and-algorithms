from node import Node
from bst import BST as tree

def fizz_the_buzz(Node):
    """
    Function that replaces node values with appropriate string
    """
    if (Node.val % 15 == 0):
        Node.val = 'fizzbuzz'
        return Node
    if (Node.val % 5 == 0):
        Node.val = 'buzz'
        return Node
    if (Node.val % 3 == 0):
        Node.val = 'fizz'
        return Node
    else:
        return Node

def fizzbuzztree(tree):
    """
    Calls fizz_the_buzz function on a tree
    """
    tree.in_order(fizz_the_buzz)
    return tree
