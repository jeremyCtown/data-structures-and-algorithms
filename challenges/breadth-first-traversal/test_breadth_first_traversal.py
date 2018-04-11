import pytest
from breadth_first_traversal import breadth_first_traversal as bft

def test_bst_empty(test_bst):
    """
    Tests a bst with no values added is empty
    """
    assert test_bst.root is None
    assert test_bst.iter == []
    test_bst.insert(5)
    assert test_bst.root.val == 5
    

def test_iterable_tree(iterable):
    """
    Tests a full bst with bft
    """
    assert bft(iterable) == [6, 3, 15, 1, 5, 8, 30, 2, 13]
    

