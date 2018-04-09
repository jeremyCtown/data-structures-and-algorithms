
def test_bst_empty(test_bst):
    """

    """
    assert test_bst.root is None


def test_bst_insertion(test_bst):
    """

    """
    test_bst.insert([5])
    assert test_bst.root.val == [5]


def test_iterable_insertion(iterable):
    """

    """
    assert iterable.root.val == 8
    assert iterable.root.left.val == 2
    assert iterable.root.right.val == 18
    assert iterable.root.left.left.val == 1
    assert iterable.root.left.right.val == 5
    assert iterable.root.right.left.val == 13
    assert iterable.root.right.right.val == 23


def test_bst_in_order(iterable):
    """

    """
    output = []

    def operation(thing):
        output.append(thing.val)

    iterable.in_order(operation)
    assert output == [1, 2, 5, 8, 13, 18, 23]


def test_bst_pre_order(iterable):
    """

    """
    output = []

    def operation(thing):
        output.append(thing.val)

    iterable.pre_order(operation)
    assert output == [8, 2, 1, 5, 18, 13, 23]


def test_bst_post_order(iterable):
    """

    """
    output = []

    def operation(thing):
        output.append(thing.val)

    iterable.post_order(operation)
    assert output == [1, 5, 2, 13, 23, 18, 8]
