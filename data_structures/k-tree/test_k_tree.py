
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


def test_ktree_insert_no_parent_adds_children_to_root(test_ktree):
    """Test children are added to root if no parent provided."""
    test_ktree.insert(5)
    test_ktree.insert(6)
    assert test_ktree.root.val == 5
    assert str(test_ktree.root.children[0]) == 'Val: 6, Children: []'
    assert test_ktree._size == 2


def test_ktree_inserts_at_parent_node(test_ktree):
    """Test that child is attached to parent."""
    test_ktree.insert(5)
    test_ktree.insert(6)
    test_ktree.insert(8, 6)
    assert test_ktree.root.val == 5
    assert str(test_ktree.root.children) == '[Val: 6, Children: [Val: 8, Children: []]]'
    assert test_ktree._size == 3