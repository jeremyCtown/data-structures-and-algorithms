import pytest

from selection import selection_smallest_first, selection_largest_first

def test_selection_smallest_random():
    """Test randomly ordered list."""
    lst = [54,26,93,17,77,31,44,55,20]
    assert selection_smallest_first(lst) == [17, 20, 26, 31, 44, 54, 55, 77, 93]


def test_selection_smallest_nearly_ordered():
    """Test nearly ordered list."""
    lst = [1, 2, 3, 4, 6, 7, 8, 9, 5]
    assert selection_smallest_first(lst) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_selection_smallest_reverse_ordered():
    """Test reverse ordered list."""
    lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert selection_smallest_first(lst) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_selection_smallest_two_values():
    """Test list with two repeated values."""
    lst = [8, 3, 8, 3, 8, 3, 8, 8, 3, 3]
    assert selection_smallest_first(lst) == [3, 3, 3, 3, 3, 8, 8, 8, 8, 8]


def test_selection_largest_random():
    """Test randomly ordered list."""
    lst = [54,26,93,17,77,31,44,55,20]
    assert selection_largest_first(lst) == [17, 20, 26, 31, 44, 54, 55, 77, 93]


def test_selection_largest_nearly_ordered():
    """Test nearly ordered list."""
    lst = [1, 2, 3, 4, 6, 7, 8, 9, 5]
    assert selection_largest_first(lst) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_selection_largest_reverse_ordered():
    """Test reverse ordered list."""
    lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert selection_largest_first(lst) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_selection_largest_two_values():
    """Test list with two repeated values."""
    lst = [8, 3, 8, 3, 8, 3, 8, 8, 3, 3]
    assert selection_largest_first(lst) == [3, 3, 3, 3, 3, 8, 8, 8, 8, 8]

