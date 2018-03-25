import pytest
# import shift-array
from shift_array import ShiftArray as SA


@pytest.fixture
def test_sa():
    test_list = [3, 4, 5, 7, 8]
    test_num = 6
    return SA(test_list, test_num)


@pytest.fixture
def other_sa():
    test_list = [3, 4, 5, 7, 8, 9]
    test_num = 6
    return SA(test_list, test_num)


def test_sa_counter_list_len_odd(test_sa):
    """
    function that tests to see if counter adds up based on list length
    """
    assert test_sa.counter == 0
    test_sa.increment_counter(test_sa.test_list)
    assert test_sa.counter == 5


def test_sa_counter_list_len_even(other_sa):
    """
    function that tests to see if counter adds up based on list length
    """
    assert other_sa.counter == 0
    other_sa.increment_counter(other_sa.test_list)
    assert other_sa.counter == 6


def test_sa_insert_index_odd(test_sa):
    test_sa.split_counter(5)
    assert test_sa.insert_index == 2.5


def test_sa_insert_index_even(other_sa):
    other_sa.split_counter(6)
    assert other_sa.insert_index == 3


def test_sa_new_list_odd(test_sa):
    """
    function to ensure empty list to populate is available
    """
    test_sa.insert_shift_array(test_sa.test_list, test_sa.test_num, 2.5)
    assert test_sa.zero == 6
    assert test_sa.new_list == [3, 4, 5, 6, 7, 8]


def test_sa_new_list_even(other_sa):
    """
    function to ensure empty list to populate is available
    """
    other_sa.insert_shift_array(other_sa.test_list, other_sa.test_num, 3)
    assert other_sa.zero == 7
    assert other_sa.new_list == [3, 4, 5, 6, 7, 8, 9]
