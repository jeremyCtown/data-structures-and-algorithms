
def test_bst_empty(test_bst):
    """
    Tests a bst with no values added is empty
    """
    assert test_bst.root is None
    assert test_bst.iter == []


def test_bst_insertion(test_bst):
    """
    Tests insert function to empty BST
    """
    test_bst.insert([5])
    assert test_bst.root.val == [5]


def test_iterable_insertion(iterable):
    """
    Tests iterable insertion
    """
    assert iterable.root.val == 8
    assert iterable.root.left.val == 2
    assert iterable.root.right.val == 18
    assert iterable.root.left.left.val == 1
    assert iterable.root.left.right.val == 5
    assert iterable.root.right.left.val == 13
    assert iterable.root.right.right.val == 23


def test_dict_insertion(test_dict):
    """
    Tests single dict insertion
    """
    assert test_dict.root.val == {'foo': 'bar'}


def test_bst_in_order(test_bst):
    """
    Tests in_order method
    """
    output = []

    test_bst.insert(8)
    test_bst.in_order(lambda thing: output.append(thing.val))
    assert output[0] == 8


def test_string_in_order(iterable):
    """
    Tests in_order method for iterable
    """
    output = []

    iterable.in_order(lambda thing: output.append(thing.val))
    assert output == [1, 2, 5, 8, 13, 18, 23]


def test_bst_pre_order(test_bst):
    """
    Tests pre_order basic functionality
    """
    output = []

    test_bst.insert(8)
    test_bst.pre_order(lambda thing: output.append(thing.val))
    assert output[0] == 8


def test_iterable_pre_order(iterable):
    """
    Tests pre_order for iterable
    """
    output = []

    iterable.pre_order(lambda thing: output.append(thing.val))
    assert output == [8, 2, 1, 5, 18, 13, 23]


def test_bst_post_order(test_bst):
    """
    Tests post_order basic functionality
    """
    output = []

    test_bst.insert(8)
    test_bst.post_order(lambda thing: output.append(thing.val))
    assert output[0] == 8


def test_iterable_post_order(iterable):
    """
    Tests post_order for iterable
    """
    output = []

    iterable.post_order(lambda thing: output.append(thing.val))
    assert output == [1, 5, 2, 13, 23, 18, 8]
