from bst import BST


def tree_intersection(bst1, bst2):
    """Take two sets and intersect them."""
    list1 = []
    list2 = []
    answer = set() 

    bst1.traverse(lambda thing: list1.append(thing.val))
    bst2.traverse(lambda thing: list2.append(thing.val))

    for item in list1:
        for thing in list2:
            if item == thing:
                answer.add(item)

    return answer

