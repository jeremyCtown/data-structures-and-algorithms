import pytest

from selection import selection_smallest_first, selection_largest_first

def test_selection_smallest():
    lst = [54,26,93,17,77,31,44,55,20]
    assert selection_smallest_first(lst) == [17, 20, 26, 31, 44, 54, 55, 77, 93]


def test_selection_largest():
    lst = [54,26,93,17,77,31,44,55,20]
    assert selection_smallest_first(lst) == [17, 20, 26, 31, 44, 54, 55, 77, 93]

