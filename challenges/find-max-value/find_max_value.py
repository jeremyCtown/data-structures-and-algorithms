from bst import BST as tree



def find_max_value(tree):
    """
    Prints out bst from top to bottom, left to right
    """
    
    max_val = 0

    def max_finder(val, max_val):
        if val > max_val:
            max_val = val
        return max_val
        
    tree.in_order(max_finder)

    return max_val