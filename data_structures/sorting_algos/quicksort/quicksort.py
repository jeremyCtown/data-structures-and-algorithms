
def quicksort(lst):
    """Recursive function to order a list quickly."""
    right = []
    equal = []
    left = []

    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        for item in lst:
            if item < pivot:
                right.append(item)
            if item == pivot:
                equal.append(item)
            if item > pivot:
                left.append(item)
        return quicksort(right)+equal+quicksort(left)
