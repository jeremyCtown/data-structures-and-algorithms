from fizzbuzztree import fizzbuzztree


def test_basic_function_bst(test_bst):
    assert test_bst.root is None
    test_bst.insert(15)
    assert test_bst.root.val == 15
    test_bst.in_order(fizzbuzztree)
    assert test_bst.root.val == 'fizzbuzz'
    

def test_tree_iterable_fbt(iterable):
    assert iterable.root.val == 6
    iterable.in_order(fizzbuzztree)
    assert iterable.root.val == 'fizz'
    assert iterable.root.left.val == 'fizz'
    assert iterable.root.right.val == 'fizzbuzz'
    assert iterable.root.left.left.val == 1
    assert iterable.root.left.right.val == 'buzz'
    assert iterable.root.right.left.val == 8
    assert iterable.root.right.right.val == 'fizzbuzz'