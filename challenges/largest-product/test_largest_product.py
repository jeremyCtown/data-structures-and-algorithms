import pytest
import largest_product as lp


def test_largest_product():
    assert lp.largest_product([[1, 2], [2, 3], [3, 4], [4, 5]]) == 20


def test_largest_product_middle():
    assert lp.largest_product([[3, 5], [7, 4], [8, 5]]) == 40


def test_single_data_lists():
    with pytest.raises(TypeError):
        lp.largest_product([[1], [2]])

