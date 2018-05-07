from bst import BST as tree


def find_max_value(tree):
    """
    Returns max value from a tree
    """
    tree.in_order(set_root_value)
    return tree.root.val

def set_root_value(tree, node):
    """
    Sets root value to greatest value in tree
    """
    if tree.root.val is None:
        raise AttributeError

    if tree.root.val < node.val:
        tree.root.val = node.val
