import pytest
import binary_search as bs


def test_if_int_in_list():
    """
    function that tests to see if the integer is in the list
    """
    search_list = [1, 2, 4, 5, 6]
    new_integer = 4
    assert bs.binary_search == 2


def test_not_in_list():
    """
    see if number is not in list
    """
    search_list = [1, 2, 4, 5, 6]
    new_integer = 3
    assert bs.binary_search == -1
