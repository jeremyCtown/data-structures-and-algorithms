import pytest
from multi_bracket_validation import multi_bracket_validation as mb

stuff = '()'
broken_stuff = '[)'


def test_for_stuff():
    assert mb(stuff) is True


def test_for_broken_stuff():
    assert mb(broken_stuff) is False


more_stuff = '([{}])'
more_broken_stuff = '({[]}]'


def test_for_more_stuff():
    assert mb(more_stuff) is True


def test_for_more_broken_stuff():
    assert mb(broken_stuff) is False


crazy_stuff = '(){some_text[more_text]()}'
broke_AF = '(){some_text[more_text}()]'


def test_for_crazy_stuff():
    assert mb(crazy_stuff) is True


def test_for_broke_AF():
    assert mb(broke_AF) is False
