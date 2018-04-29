def test_ktree_empty(test_ktree):
    """Test ktree with no values added is empty."""
    assert test_ktree.root is None
    assert test_ktree._size == 0


def test_ktree_insertion(test_ktree):
    """Test insert single value to empty ktree."""
    test_ktree.insert(5)
    assert test_ktree.root.val == 5
    assert test_ktree.root.children == []
    assert test_ktree._size == 1