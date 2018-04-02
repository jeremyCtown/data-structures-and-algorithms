

def test_insert_first_node(empty_ll):
    assert empty_ll.head is None
    empty_ll.insert(2)
    assert empty_ll.head.val == 2


def test_insert_first_node_iterable(small_ll):
    assert small_ll.head.val == 5
    small_ll.insert(2)
    assert small_ll.head.val == 2


def test_append_adds_to_end(long_ll):
    assert long_ll._size == 10
    assert long_ll.append(2) is None
    assert long_ll._size == 11


def test_insert_before(small_ll):
    assert small_ll._size == 4
    small_ll.insert_before(8, 7)
    assert small_ll._size == 5
    assert small_ll.head._next._next.val == 7
    assert small_ll.head._next._next._next.val == 8


def test_insert_after(small_ll):
    assert small_ll._size == 4
    small_ll.insert_after(6, 7)
    assert small_ll._size == 5
    assert small_ll.head._next.val == 6
    assert small_ll.head._next._next.val == 7


def test_kth_from_end(empty_ll):
    assert empty_ll._size == 0
    empty_ll.insert(2)
    empty_ll.insert(3)
    empty_ll.insert(4)
    assert empty_ll.kth_from_end(2).val == 3


def test_kth_from_end_edge(empty_ll):
    assert empty_ll.kth_from_end(1) is None


def test_kth_from_end_iterable(long_ll):
    assert long_ll._size == 10
    assert long_ll.kth_from_end(3).val == 8
