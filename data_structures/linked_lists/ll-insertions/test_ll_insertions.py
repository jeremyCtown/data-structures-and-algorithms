

def test_insert_first_node(empty_ll):
    assert empty_ll.head is None
    empty_ll.insert(2)
    assert empty_ll.head.val == 2


def test_insert_additional_node(small_ll):
    assert small_ll.head.val == 5
    small_ll.insert(10)
    assert small_ll.head.val == 10


def test_append_adds_to_empty(empty_ll):
    assert empty_ll._size == 0
    empty_ll.append(2)
    assert empty_ll._size == 1
    assert empty_ll.head.val == 2


def test_append_adds_to_end(small_ll):
    assert small_ll._size == 4
    assert small_ll.append(2).val == 2
    assert small_ll._size == 5


def test_insert_before_size(small_ll):
    assert small_ll._size == 4
    small_ll.insert_before(8, 7)
    assert small_ll._size == 5
    assert small_ll.head._next._next.val == 7
    assert small_ll.head._next._next._next.val == 8


def test_insert_before_empty_list(empty_ll):
    empty_ll.insert(8)
    assert empty_ll.head.val == 8
    empty_ll.insert_before(8, 7)
    assert empty_ll.head.val == 7
    assert empty_ll._size == 2


def test_insert_after_size(small_ll):
    assert small_ll._size == 4
    small_ll.insert_after(6, 7)
    assert small_ll._size == 5
    assert small_ll.head._next.val == 6
    assert small_ll.head._next._next.val == 7


def test_insert_after_empty_list(empty_ll):
    empty_ll.insert(8)
    assert empty_ll.head.val == 8
    assert empty_ll.insert_after(8, 9).val == 9
    assert empty_ll.head.val == 8
    assert empty_ll._size == 2
