

def test_initial_of_list(test_ll):
    assert test_ll._size == 0
    assert test_ll.head is None
    assert test_ll._current is None
    assert test_ll.iter == []


def test_insert_of_val(test_ll):
    test_ll.insert([1, 2, 3, 4])
    assert test_ll._size == 1
    test_ll.insert(0)
    assert test_ll._size == 2


def test_insert_first_node(test_ll):
    assert test_ll.head is None
    test_ll.insert(2)
    assert test_ll.head.val == 2


def test_find_a_val_in_ll(short_ll):
    assert short_ll.find(1) is True
    assert short_ll.find(5) is False



