from bst import BST
import pytest

@pytest.fixture
def test_bst():
    return BST([8, 2, 5, 18, 13, 1, 23])


@pytest.fixture
def test_bst2():
    return BST([3, 8, 6, 18, 13, 9, 23])


@pytest.fixture
def empty_bst():
    return BST()