import pytest
import largest_product as LP

test_list = [[1, 2], [2, 3], [3, 4], [4, 5]]
new_list = [2, 6, 12, 20]
answer = 420

test_2 = [[1, 3], [5, 6], [1, 2], [0, 0]]
new_2 = [3, 30, 2, 0]
answer_2 = 90

test_3 = [[5], [5]]
new_3 = [5, 5]
answer_3 = 25


def test_multiply_inner_lists_1():
    assert LP.multiply_inner_lists(test_list) == new_list


def test_multiply_inner_lists_2():
    assert LP.multiply_inner_lists(test_2) == new_2


def test_multiply_inner_lists_3():
    assert LP.multiply_inner_lists(test_3) == new_3


def test_largest_product_1():
    assert LP.largest_product(new_list) == answer


def test_largest_product_2():
    assert LP.largest_product(new_2) == answer_2


def test_largest_product_3():
    assert LP.largest_product(new_3) == answer_3


# def test_largest_product(test_lp):
#     test_lp.new_list = [2, 6, 12, 20]
#     test_lp.largest_product()
#     assert test_lp.new_list == [2, 6, 12, 20]
#     assert test_lp.answer is not str
#     assert test_lp.answer == 20
