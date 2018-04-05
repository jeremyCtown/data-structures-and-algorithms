import pytest
from multi_bracket_validation import multi_bracket_validation as mb

stuff = '[]'


def test_for_stuff():

    assert mb(stuff) is True
