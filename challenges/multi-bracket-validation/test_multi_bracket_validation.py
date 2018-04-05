import pytest
from multi_bracket_validation import multi_bracket_validation as mb

stuff = '()'
broken_stuff = '[)'


def test_for_stuff():
    assert mb(stuff) is True


def test_for_broken_stuff():
    assert mb(broken_stuff) is False
