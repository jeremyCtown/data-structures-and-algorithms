

def test_initial_of_list(test_ll):
    assert test_ll._size == 0
    assert test_ll.head is None
    assert test_ll._current is None
    assert test_ll.iter == []


def test_insert_val_increase_size(test_ll):
    test_ll.insert([1, 2, 3, 4])
    assert test_ll._size == 1
    test_ll.insert(0)
    assert test_ll._size == 2
    test_ll.insert(1)
    test_ll.insert(1)
    test_ll.insert(1)
    assert test_ll._size == 5


def test_iter_reverses(short_ll):
    assert short_ll.head.val == 1
    assert short_ll.head._next.val == 2
    assert short_ll.head._next._next._next._next is None


def test_insert_first_node(test_ll):
    assert test_ll.head is None
    test_ll.insert(2)
    assert test_ll.head.val == 2
    assert test_ll.head._next is None


def test_find_a_val_in_ll(short_ll):
    assert short_ll._size == 4
    assert short_ll.find(1) is True
    assert short_ll.find(5) is False



