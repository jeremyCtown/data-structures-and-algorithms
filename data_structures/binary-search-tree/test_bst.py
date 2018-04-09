
def test_bst_empty(test_bst):
    """

    """
    assert test_bst.root is None


# def test_bst_insertion(test_bst):
#     """

#     """
#     test_bst.insert([5])
#     assert test_bst.root.val == [5]


def test_iterable_insertion(iterable):
    assert iterable.root.val == 8
    assert iterable.root.left.val == 2
    assert iterable.root.right.val == 18
    assert iterable.root.left.right.val == 5
    assert iterable.root.right.left.val == 13
