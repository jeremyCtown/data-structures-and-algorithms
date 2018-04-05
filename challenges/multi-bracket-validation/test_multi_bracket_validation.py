import pytest
from multi-bracket-validation import multi_bracket_validation as mb

stuff = 'stuff'

def test_for_stuff():
    assert mb(stuff) == 'stuff'
