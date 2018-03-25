import pytest
from binary_search import BinarySearch as BS

@pytest.fixture
def test_bs():
    test_list = [3, 4, 5, 6, 7]
    test_num = 6
    return BS(test_list, test_num)

@pytest.fixture
def test_bs_fail():
    test_list = [3, 4, 5, 6, 7]
    test_num = 8
    return BS(test_list, test_num)


def test_init_counter_is_zero(test_bs):
    """
    check to make sure counter starts at 0
    """
    assert test_bs.counter == 0


def test_if_int_in_list(test_bs):
    """
    function that tests to see if the integer is in the list
    """
    test_bs.binary_search()
    assert test_bs.answer == 3


def test_not_in_list(test_bs_fail):
    """
    see if number is not in list
    """
    test_bs_fail.binary_search()
    assert test_bs_fail.answer == -1
