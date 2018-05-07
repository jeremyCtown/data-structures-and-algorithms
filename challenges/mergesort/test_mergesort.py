import pytest
from find_max_value import find_max_value as fmv

def test_bst_empty(test_bst):
    """
    Tests an empty_bst is empty and fmv raises Error
    """
    assert test_bst.root is None
    assert test_bst.iter == []
    with pytest.raises(AttributeError):
        fmv(test_bst)


def test_insertion_and_fmv(test_bst):
    """
    Tests basic functionality of fmv
    """
    test_bst.insert(5)
    assert test_bst.root.val == 5
    assert fmv(test_bst) == 5
    

def test_iterable_tree(iterable):
    """
    Tests a full bst with fmv
    """
    assert iterable.root.val == 6
    assert fmv(iterable) == 30
    

