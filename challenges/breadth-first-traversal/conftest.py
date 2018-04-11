import pytest
from bst import BST

@pytest.fixture
def test_bst():
    return BST()


@pytest.fixture
def iterable():
    return BST([6, 3, 15, 1, 5, 8, 13, 30, 2])

