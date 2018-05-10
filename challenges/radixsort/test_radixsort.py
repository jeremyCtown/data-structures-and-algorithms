import pytest
from radixsort import radixsort


def test_empty_list_returns_empty_list():
    """Test radixsort on empty list returns same."""
    empty = []
    assert radixsort(empty) == []


def test_list_with_one_value():
    """Test radixsort on empty list returns same."""
    lst = [8]
    assert radixsort(lst) == [8]


def test_list_with_two_values():
    """Test radixsort on empty list returns same."""
    lst = [18, 3]
    assert radixsort(lst) == [3, 18]


def test_list_with_odd_number_of_values():
    """Test odd number of values returns ordered list."""
    lst = [18, 3, 27, 49, 95]
    assert radixsort(lst) == [3, 18, 27, 49, 95]


def test_list_with_triple_digits():
    """Test list heavy weighted on one half returns ordered list."""
    lst = [22, 44, 33, 88, 11, 99, 0, 113]
    assert radixsort(lst) == [0, 11, 22, 33, 44, 88, 99, 113]

