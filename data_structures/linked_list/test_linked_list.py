import pytest
from linked_list import LinkedList as LL
from node import Node


@pytest.fixture
def test_node():
    return Node(1, None)

@pytest.fixture
def test_ll():
    return LL()


def test_node_exists(test_node):
    assert Node.val == 1
