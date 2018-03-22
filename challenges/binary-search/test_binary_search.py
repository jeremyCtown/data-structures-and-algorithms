import pytest
import binary_search as bs


def test_if_int_in_list():
    """
    function that tests to see if the integer is in the list
    """
    search_list = [1, 2, 4, 5, 6]
    new_integer = 4
    assert new_integer in search_list == True
    assert new_integer not in search_list == False

def test_counter_same_as_index():
    """
    see if counter is the same as the index number of the matching number
    """
    counter = 1
    i = 1
    assert counter == i
