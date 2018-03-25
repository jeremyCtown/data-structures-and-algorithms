import pytest
from largest_product import LargestProduct as LP

@pytest.fixture
def test_lp():
    test_list = [[1, 2], [2, 3], [3, 4], [4, 5]]
    return LP(test_list)


def test_input_is_valid(test_lp):
    assert test_lp.test_list == [[1, 2], [2, 3], [3, 4], [4, 5]]
    assert test_lp.counter == 0
    assert test_lp.answer == 0


def test_multiply_inner_lists(test_lp):
    test_lp.multiply_inner_lists()
    assert test_lp.counter == 4
    assert test_lp.new_list[0] is not str
    assert test_lp.new_list == [2, 6, 12, 20]


def test_largest_product(test_lp):
    test_lp.new_list = [2, 6, 12, 20]
    test_lp.largest_product()
    assert test_lp.new_list == [2, 6, 12, 20]
    assert test_lp.answer is not str
    assert test_lp.answer == 20


# def test_if_int_in_list():
#     """
#     test if two numbers at i add together
#     """
#     test_list = [2, 3]
#     assert ls.sum_inner_lists == 6



# def test_largest_product():
#     """
#     see if number is not in list
#     """
#     test_list = [12, 13]
#     assert bs.binary_search == 13
