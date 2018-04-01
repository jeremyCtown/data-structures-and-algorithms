import pytest
from largest_product import LargestProduct as LP


def test_create_new_list():
    test_list = [[1, 2], [2, 3], [3, 4], [4, 5]]
    assert LP.create_new_list(test_list) == [1, 2, 2, 3, 3, 4, 4, 5]



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
