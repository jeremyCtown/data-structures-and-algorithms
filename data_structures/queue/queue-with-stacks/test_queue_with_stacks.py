import pytest
from queue_with_stacks import Queue

@pytest.fixture
def empty_queue():
    return Queue()


def test_enqueue_functionality(empty_queue):
    assert empty_queue._size == 0
    empty_queue.enqueue(1)
    empty_queue.enqueue(2)
    assert empty_queue._size == 2


def test_dequeue_functionality(small_queue):
    assert small_queue._size == 5
    small_queue.dequeue()
    assert small_queue._size == 4

def test_interoperability(small_queue):
    assert small_queue._size == 5
    small_queue.dequeue()
    small_queue.dequeue()
    assert small_queue._size == 3
    small_queue.enqueue(8)
    small_queue.enqueue(9)
    assert small_queue._size == 5





# def test_dequeue_small_input(small_queue):
#     assert small_queue._size == 5
#     assert small_queue.dequeue().val == 4
#     assert small_queue.front.val == 5
#     assert small_queue._size == 4


# def test_dequeue_large_input(large_queue):
#     assert large_queue._size == 1000
#     assert large_queue.dequeue().val == 0
#     assert large_queue.front.val == 1
#     assert large_queue._size == 999


def test_dequeue_edge_empty_list(empty_queue):
    assert empty_queue.dequeue() is None
