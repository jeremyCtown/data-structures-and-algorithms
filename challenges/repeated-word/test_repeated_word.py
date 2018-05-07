from repeated_word import repeated_word as rw

def test_repeated_word():
    """Test repeated word comes back."""
    assert rw('this is this') == 'this'