import pytest


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


def test_ktree_pre_order_on_empty_throws_exception(test_ktree):
    """Test error raise for empty ktree with pre_order."""
    output = []
    with pytest.raises(IndexError):
        test_ktree.pre_order(lambda thing: output.append(thing.val))


def test_ktree_pre_order_traversal_simple(test_ktree):
    """Test pre_order method for single insertion."""
    output = []

    test_ktree.insert(8)
    test_ktree.pre_order(lambda thing: output.append(thing.val))
    assert output[0] == 8


def test_ktree_pre_order_traversal_multiple_values(test_ktree):
    """Test pre_order method for multiple insertions."""
    output = []

    test_ktree.insert(5)
    test_ktree.insert(6)
    test_ktree.insert(8, 6)
    test_ktree.insert(9, 5)
    test_ktree.insert(10, 5)
    test_ktree.insert(3, 8)
    test_ktree.insert(2, 8)
    test_ktree.insert(1, 2)
    test_ktree.pre_order(lambda thing: output.append(thing.val))
    assert output == [5, 6, 8, 3, 2, 1, 9, 10]


def test_ktree_post_order_on_empty_throws_exception(test_ktree):
    """Test error raise for empty ktree with post_order."""
    output = []
    with pytest.raises(IndexError):
        test_ktree.post_order(lambda thing: output.append(thing.val))


def test_ktree_post_order_traversal_simple(test_ktree):
    """Test post_order method for single insertion."""
    output = []

    test_ktree.insert(8)
    test_ktree.post_order(lambda thing: output.append(thing.val))
    assert output[0] == 8


def test_ktree_post_order_traversal_multiple_values(test_ktree):
    """Test post_order method for multiple insertions."""
    output = []

    test_ktree.insert(5)
    test_ktree.insert(6)
    test_ktree.insert(8, 6)
    test_ktree.insert(9, 5)
    test_ktree.insert(10, 5)
    test_ktree.insert(3, 8)
    test_ktree.insert(2, 8)
    test_ktree.insert(1, 2)
    test_ktree.post_order(lambda thing: output.append(thing.val))
    assert output == [3, 1, 2, 8, 6, 9, 10, 5]


def test_ktree_breadth_first_traversal_on_empty_throws_exception(test_ktree):
    """Test error raise for empty ktree with breadth_first_traversal."""
    output = []
    with pytest.raises(IndexError):
        test_ktree.breadth_first_traversal(lambda thing: output.append(thing))


def test_ktree_breadth_first_traversal_traversal_simple(test_ktree):
    """Test breadth_first_traversal method for single insertion."""
    output = []

    test_ktree.insert(8)
    test_ktree.breadth_first_traversal(lambda thing: output.append(thing.val))
    assert output[0] == 8


def test_ktree_breadth_first_traversal_traversal_multiple_values(test_ktree):
    """Test breadth_first_traversal method for multiple insertions."""
    output = []

    test_ktree.insert(5)
    test_ktree.insert(6)
    test_ktree.insert(8, 6)
    test_ktree.insert(9, 5)
    test_ktree.insert(10, 5)
    test_ktree.insert(3, 8)
    test_ktree.insert(2, 8)
    test_ktree.insert(1, 2)
    test_ktree.breadth_first_traversal(lambda thing: output.append(thing.val))
    assert output == [5, 6, 9, 10, 8, 3, 2, 1]