import pytest
from stack import Stack


def test_empty_stack_has_no_top(empty_stack):
    assert empty_stack.top is None


def test_current_size(small_stack):
    assert small_stack._size == 5


def test_insertion_of_value(empty_stack):
    assert empty_stack.top is None
    assert empty_stack.push(1).val == 1
    assert empty_stack.top.val == 1


def test_insertion_current_top(small_stack):
    assert small_stack.top.val == 8


def test_insertion_large_list(large_stack):
    assert large_stack.top.val == 999


def test_pop_functionality(empty_stack):
    assert empty_stack.push(8).val == 8
    assert empty_stack.pop() == 8


def test_pop_for_real(large_stack):
    assert large_stack.pop() == 999


def test_pop_edge_empty_list(empty_stack):
    with pytest.raises(IndexError):
        empty_stack.pop()


def test_peek_user_gen_list(small_stack):
    assert small_stack.peek() == 8


def test_peek_for_real(large_stack):
    assert large_stack.peek() == 999


def test_peek_edge_empty_list(empty_stack):
    with pytest.raises(IndexError):
        empty_stack.peek()
