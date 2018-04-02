import pytest
from stack import Stack


def test_empty_stack_has_no_top(empty_stack):
    assert empty_stack.top is None


def test_insertion_of_value(empty_stack):
    assert empty_stack.top is None
    assert empty_stack.push(1).val == 1


def test_empty_val_on_insert(empty_stack):
    with pytest.raises(TypeError):
        empty_stack.push()


def test_non_int_val(empty_stack):
    with pytest.raises(TypeError):
        empty_stack.push('not a number')


def test_pop_functionality(empty_stack):
    assert empty_stack.push(8).val == 8
    assert empty_stack.pop().val == 8


def test_pop_for_real(large_stack):
    assert large_stack.pop().val == 999


def test_pop_edge_empty_list(empty_stack):
    assert empty_stack.pop() is None


def test_peek_user_gen_list(small_stack):
    assert small_stack.peek().val == 8


def test_peek_for_real(large_stack):
    assert large_stack.peek().val == 999


def test_peek_edge_empty_list(empty_stack):
    assert empty_stack.peek() is None
