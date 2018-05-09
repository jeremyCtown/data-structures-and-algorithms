import pytest
from mergesort import mergesort, merge


def test_empty_list_returns_empty_list():
    """Test mergesort on empty list returns same."""
    empty = []
    assert mergesort(empty) == []


def test_list_with_one_value():
    """Test mergesort on empty list returns same."""
    lst = [8]
    assert mergesort(lst) == [8]


def test_list_with_two_values():
    """Test mergesort on empty list returns same."""
    lst = [8, 3]
    assert mergesort(lst) == [3, 8]


def test_list_with_odd_number_of_values():
    """Test odd number of values returns ordered list."""
    lst = [8, 3, 7, 9, 5]
    assert mergesort(lst) == [3, 5, 7, 8, 9]


def test_list_with_unbalanced_halves():
    """Test list heavy weighted on one half returns ordered list."""
    lst = [2, 4, 3, 8, 1, 9, 10, 13]
    assert mergesort(lst) == [1, 2, 3, 4, 8, 9, 10, 13]


def test_merge_merges_two_pairs():
    """Test merge function separate of mergesort."""
    L = [1, 3, 5]
    R = [2, 4, 6]
    assert merge(L, R) == [1, 2, 3, 4, 5, 6]


def test_merge_merges_uneven_lists():
    L = [1, 3, 5]
    R = [2, 4]
    assert merge(L, R) == [1, 2, 3, 4, 5]


def test_merge_on_unbalanced_lists():
    """Test list heavy weighted on one half returns ordered list."""
    L = [2, 3, 4, 8]
    R =  [1, 9, 10, 13]
    assert merge(L, R) == [1, 2, 3, 4, 8, 9, 10, 13]


    

