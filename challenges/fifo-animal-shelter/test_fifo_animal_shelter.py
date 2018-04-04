
def test_empty_queue_has_no_back(empty_queue):
    assert empty_queue.back is None
    assert empty_queue.front is None


def test_current_size(small_queue):
    assert small_queue._size == 5


def test_insertion_of_value(empty_queue):
    assert empty_queue.back is None
    assert empty_queue.enqueue('dog').val == 'dog'
    assert empty_queue.back.val == 'dog'


def test_insertion_current_back(small_queue):
    assert small_queue._size == 5
    assert small_queue.back.val == 'dog'
    assert small_queue.front.val == 'cat'


def test_dequeue_functionality(empty_queue):
    assert empty_queue.enqueue('dog') == 'dog'
    assert empty_queue.dequeue('dog').val == 'dog'
    assert empty_queue._size == 0

def test_dequeue_small_list(small_list):
    assert small_queue.dequeue('dog') == 'dog'
    assert small_queue._size == 4

