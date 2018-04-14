from fizzbuzztree import fizzbuzztree


def test_basic_function_bst(test_bst):
    """
    Tests basic interactivity between tree and fizzbuzztree function
    """
    assert test_bst.root is None
    test_bst.insert(15)
    test_bst.insert(3)
    test_bst.insert(20)
    assert test_bst.root.val == 15
    assert test_bst.root.left.val == 3
    assert test_bst.root.right.val == 20 
    fizzbuzztree(test_bst)
    assert test_bst.root.val == 'fizzbuzz'
    assert test_bst.root.left.val == 'fizz'
    assert test_bst.root.right.val == 'buzz'    


def test_tree_iterable_fbt(iterable):
    """
    Tests full functionality of BST and fizzbuzztree on iterable
    """
    assert iterable.root.val == 6
    fizzbuzztree(iterable)
    assert iterable.root.val == 'fizz'
    assert iterable.root.left.val == 'fizz'
    assert iterable.root.right.val == 'fizzbuzz'
    assert iterable.root.left.left.val == 1
    assert iterable.root.left.right.val == 'buzz'
    assert iterable.root.right.left.val == 8
    assert iterable.root.right.right.val == 'fizzbuzz'


def test_empty_tree_returns_none(test_bst):
    """
    Tests fizzbuzztree on empty tree returns None
    """
    assert test_bst.root is None
    fizzbuzztree(test_bst)
    assert test_bst.root is None