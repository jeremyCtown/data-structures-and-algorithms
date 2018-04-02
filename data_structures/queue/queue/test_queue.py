import pytest
from queue import Queue


def test_empty_queue_has_no_back(empty_queue):
    assert empty_queue.back is None
    assert empty_queue.front is None


def test_current_size(small_queue):
    assert small_queue._size == 5


def test_insertion_of_value(empty_queue):
    assert empty_queue.back is None
    assert empty_queue.enqueue(1).val == 1
    assert empty_queue.back.val == 1


def test_insertion_of_iterable(iter_queue):
    assert iter_queue.back.val == 9
    assert iter_queue.front.val == 7
    assert iter_queue._size == 3


def test_insertion_current_back(small_queue):
    assert small_queue._size == 5
    assert small_queue.back.val == 8
    assert small_queue.front.val == 4


def test_insertion_large_list(large_queue):
    assert large_queue._size == 1000
    assert large_queue.front.val == 0
    assert large_queue.back.val == 999


def test_dequeue_functionality(empty_queue):
    assert empty_queue.enqueue(8).val == 8
    assert empty_queue.dequeue().val == 8


def test_dequeue_small_input(small_queue):
    assert small_queue._size == 5
    assert small_queue.dequeue().val == 4
    assert small_queue.front.val == 5
    assert small_queue._size == 4


def test_dequeue_large_input(large_queue):
    assert large_queue._size == 1000
    assert large_queue.dequeue().val == 0
    assert large_queue.front.val == 1
    assert large_queue._size == 999


def test_dequeue_edge_empty_list(empty_queue):
    assert empty_queue.dequeue() is None


def test_everything(iter_queue):
    iter_queue.enqueue(10)
    assert iter_queue._size == 4
    assert iter_queue.front.val == 7
    assert iter_queue.back.val == 10
    iter_queue.dequeue()
    assert iter_queue.front.val == 8
    assert iter_queue.back.val == 10
    assert iter_queue._size == 3
    iter_queue.dequeue()
    assert iter_queue.front.val == 9
    assert iter_queue.back.val == 10
    assert iter_queue._size == 2
    iter_queue.dequeue()
    assert iter_queue.front.val == 10
    assert iter_queue.back.val == 10
    assert iter_queue._size == 1
    iter_queue.dequeue()
    assert iter_queue.front is None
    assert iter_queue.back is None
    assert iter_queue._size == 0
