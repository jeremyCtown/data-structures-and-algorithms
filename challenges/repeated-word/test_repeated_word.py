import pytest
from repeated_word import repeated_word as rw

def test_repeated_word():
    """Test repeated word comes back."""
    assert rw('this is this') == 'this'


def test_word_not_repeated():
    """Test no repeated words raise error."""
    with pytest.raises(KeyError):
        rw('no words repeat')