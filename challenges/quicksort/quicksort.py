


def quicksort(lst):
    """Recursive function to order a list quickly."""
    if len(lst) < 2:
        return lst
    else:
        midpoint = len(lst)/2
        L = quicksort(lst[midpoint::])
        R = quicksort(lst[::midpoint])
        return lst
