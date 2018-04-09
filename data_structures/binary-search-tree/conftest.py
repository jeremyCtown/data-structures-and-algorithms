import pytest
from bst import BST


@pytest.fixture
def test_bst():
    return BST()


@pytest.fixture
def iterable():
    return BST([8, 2, 5, 18, 13, 1, 23])


@pytest.fixture
def test_dict():
    return BST([{'foo': 'bar'}])
