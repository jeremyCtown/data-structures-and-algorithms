from tree_intersection import tree_intersection as ti

def test_bst_setup(test_bst):
    """Test bst is setup correctly."""
    assert test_bst.root.val == 8
    assert test_bst.iter == [8, 2, 5, 18, 13, 1, 23]


def test_bst2_setup(test_bst2):
    """Test bst2 is setup correctly."""
    assert test_bst2.root.val == 3
    assert test_bst2.iter == [3, 8, 6, 18, 13, 9, 23]


def test_bst_traverse(test_bst):
    """Test bst traversal method."""
    output = []

    test_bst.traverse(lambda thing: output.append(thing.val))
    assert output == [1, 2, 5, 8, 13, 18, 23]


def test_bst2_traverse(test_bst2):
    """Test bst2 traversal method."""
    output = []

    test_bst2.traverse(lambda thing: output.append(thing.val))
    assert output == [3, 6, 8, 9, 13, 18, 23]


def test_ti_answer_is_set(test_bst, test_bst2):
    """Test ti answer is a set."""
    assert ti(test_bst, test_bst2).__class__ == set


def test_tree_intersection(test_bst, test_bst2):
    """Test tree insertion works."""
    assert ti(test_bst, test_bst2) == {8, 13, 18, 23}


def test_ti_empty_bst_returns_empty_set(test_bst, empty_bst):
    """Test empty bst returns empty set."""
    assert ti(test_bst, empty_bst) == set([])
