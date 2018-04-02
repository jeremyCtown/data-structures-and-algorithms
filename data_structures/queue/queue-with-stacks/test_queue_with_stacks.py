import pytest
from queue_with_stacks import Queue

@pytest.fixture
def empty_queue():
    return Queue()


def test_enqueue_functionality(empty_queue):
    """
    makes sure node is passing through enqueue
    """
    assert empty_queue._size == 0
    empty_queue.enqueue(1)
    empty_queue.enqueue(2)
    assert empty_queue._size == 2


def test_dequeue_functionality(small_queue):
    """
    test dequeue adds/subtracts from size
    """
    assert small_queue._size == 5
    small_queue.dequeue()
    assert small_queue._size == 4


def test_interoperability(small_queue):
    """
    test can switch back and forth
    """
    assert small_queue._size == 5
    small_queue.dequeue()
    small_queue.dequeue()
    assert small_queue._size == 3
    small_queue.enqueue(8)
    small_queue.enqueue(9)
    assert small_queue._size == 5


def test_dequeue_edge_empty_list(empty_queue):
    assert empty_queue.dequeue() is None
