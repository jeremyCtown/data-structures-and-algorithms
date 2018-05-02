from bst import BST


def tree_intersection(bst1, bst2):
    """Take two sets and intersect them."""
    set1 = {}
    set2 = {}
    answer = {}

    bst1.traverse(lambda thing: set1.add(thing.val))
    bst2.traverse(lambda thing: set2.add(thing.val))
    
    # return set1.intersection(set2)

    for item in set1:
        for item in set2:
            if set2.item == set1.item:
                answer.add(set2.item)

    return answer

