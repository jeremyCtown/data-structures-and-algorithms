import pytest
from repeated_word import repeated_word as rw

def test_repeated_word():
    """Test repeated word comes back."""
    assert rw('this is this') == 'this'


def test_word_not_repeated():
    """Test no repeated words raise error."""
    assert rw('nothing repeats in this string') == 'No words repeat'


def test_long_string_with_multiple_repeated_words():
    """Test that the first repeated word is returned."""
    assert rw('This is a long string of words with two of the words repeated twice') == 'of'


def test_empty_string():
    """Test that the first repeated word is returned."""
    assert rw('') == 'Empty string'