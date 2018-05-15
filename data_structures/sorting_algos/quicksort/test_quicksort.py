import pytest
from quicksort import quicksort


def test_empty_list_returns_empty_list():
    """Test quicksort on empty list returns same."""
    empty = []
    assert quicksort(empty) == []


def test_list_with_one_value():
    """Test quicksort on empty list returns same."""
    lst = [8]
    assert quicksort(lst) == [8]


def test_list_with_two_values():
    """Test quicksort on empty list returns same."""
    lst = [8, 3]
    assert quicksort(lst) == [3, 8]


def test_list_with_odd_number_of_values():
    """Test odd number of values returns ordered list."""
    lst = [8, 3, 7, 9, 5]
    assert quicksort(lst) == [3, 5, 7, 8, 9]


def test_list_with_unbalanced_halves():
    """Test list heavy weighted on one half returns ordered list."""
    lst = [2, 4, 3, 8, 1, 9, 10, 13]
    assert quicksort(lst) == [1, 2, 3, 4, 8, 9, 10, 13]


def test_list_with_few_values():
    """Test list with few distinct values returns sorted list."""
    lst = [3, 1, 8, 3, 1, 23, 8, 3, 23, 1, 8, 23]
    assert quicksort(lst) == [1, 1, 1, 3, 3, 3, 8, 8, 8, 23, 23, 23]