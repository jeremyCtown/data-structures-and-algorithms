from pets import Dog, Cat
import pytest


def test_empty_queue_has_no_front_or_back(empty_queue):
    """
    Tests that queue is empty
    """
    assert empty_queue.back is None
    assert empty_queue.front is None


def test_current_size(small_queue):
    """
    Tests that size is tracked
    """
    assert small_queue._size == 5


def test_insertion_of_value(empty_queue):
    """
    Tests that enqueue works
    """
    assert empty_queue.back is None
    assert empty_queue.enqueue(Dog()).val.val == Dog().val
    assert empty_queue.back.val.val == Dog().val


def test_insertion_current_back(small_queue):
    """
    Tests that back is set to correct value
    """
    assert small_queue._size == 5
    assert small_queue.back.val.val == Cat().val
    assert small_queue.front.val.val == Cat().val


def test_dequeue_functionality(empty_queue):
    """
    Tests that enqueue and dequeue work with empty queue
    """
    empty_queue.enqueue(Dog())
    assert empty_queue.dequeue(Dog()).val == Dog().val
    assert empty_queue._size == 0


def test_no_animal_of_pref(empty_queue):
    """
    Tests that exception is raised
    """
    empty_queue.enqueue(Dog())
    with pytest.raises(Exception, message= 'We are all out of cats'):
        empty_queue.dequeue(Cat())


def test_dequeue_small_list(small_queue):
    """
    Tests removal of specific pets
    """
    assert small_queue.dequeue(Dog()).val == 'dog'
    assert small_queue._size == 4
    assert small_queue.dequeue(Cat()).val == 'cat'
    assert small_queue._size == 3

