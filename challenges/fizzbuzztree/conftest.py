import pytest
from bst import BST


@pytest.fixture
def test_bst():
    """
    Creates empty bst for testing
    """
    return BST()


@pytest.fixture
def iterable():
    """
    creates branched BST for testing
    """
    return BST([6, 3, 15, 1, 5, 8, 30])

