from fifo_animal_shelter import AnimalShelter, Dog, Cat


# def test_empty_queue_has_no_back(empty_queue):
#     assert empty_queue.back is None
#     assert empty_queue.front is None


# def test_current_size(small_queue):
#     assert small_queue._size == 5


# def test_insertion_of_value(empty_queue):
#     assert empty_queue.back is None
#     assert empty_queue.enqueue(Dog()).val.val == Dog().val
#     assert empty_queue.back.val.val == Dog().val


# def test_insertion_current_back(small_queue):
#     assert small_queue._size == 5
#     assert small_queue.back.val.val == Cat().val
#     assert small_queue.front.val.val == Cat().val


def test_dequeue_functionality(empty_queue):
    empty_queue.enqueue(Dog())
    assert empty_queue.dequeue(Dog()) == Dog()
    assert empty_queue._size == 0


def test_dequeue_small_list(small_queue):
    assert small_queue.dequeue(Dog()).val.val== 'dog'
    assert small_queue._size == 4

