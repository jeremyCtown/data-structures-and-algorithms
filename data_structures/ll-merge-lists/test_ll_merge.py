
import ll_merge as LL


def test_initial_of_list(empty_ll):
    assert empty_ll._size == 0
    assert empty_ll.head is None
    assert empty_ll._current is None


def test_insert_of_val(empty_ll):
    empty_ll.insert([1, 2, 3, 4])
    assert empty_ll._size == 1
    empty_ll.insert(0)
    assert empty_ll._size == 2


def test_insert_first_node(empty_ll):
    assert empty_ll.head is None
    empty_ll.insert(2)
    assert empty_ll.head.val == 2


def test_find_a_val_in_ll(small_ll):
    assert small_ll.find(5) is True
    assert small_ll.find(1) is False


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


def test_kth_from_end(long_ll):
    assert long_ll._size == 10
    assert long_ll.kth_from_end(3).val == 8


def test_ll_merge_long(small_ll, long_ll):
    head = LL.merge_lists(small_ll, long_ll)
    assert head.val == 1
    assert head._next.val == 5
    assert head._next._next.val == 2


def test_ll_merge_short(small_ll, single_ll):
    head = LL.merge_lists(small_ll, single_ll)
    assert head.val == 5
    assert head._next.val == 0
    assert head._next._next.val == 6


def test_ll_merge_empty(small_ll, empty_ll):
    head = LL.merge_lists(small_ll, empty_ll)
    assert head.val == 5
    assert head._next.val == 6
    assert head._next._next.val == 8
