import pytest
from linked_list import LinkedList as LL
from node import Node


@pytest.fixture
def test_node():
    return Node(1)


@pytest.fixture
def test_ll():
    return LL()


def test_initial_of_list(test_ll):
    assert test_ll._size == 0
    assert test_ll.head is None
    assert test_ll._current is None
    assert test_ll.iter == []


def test_insert_of_val(test_ll):
    test_ll.insert([1, 2, 3, 4])
    assert test_ll.head.val == [1, 2, 3, 4]



