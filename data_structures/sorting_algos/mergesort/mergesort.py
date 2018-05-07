def merge(L, R):
    """Merge two lists."""
    ordered_list = []
    while len(L) != 0 and len(R) != 0:
        if L[0] < R[0]:
            ordered_list.append(L[0])
            L.remove(L[0])
        else:
            ordered_list.append(R[0])
            R.remove(R[0])
    
    if len(L) == 0:
        ordered_list += R
    if len(R) == 0:
        ordered_list += L
    
    return ordered_list


def mergesort(lst):
    """Recursive function to order a list."""
    if len(lst) < 2:
        return lst
    else:
        midpoint = len(lst)/2
        L = mergesort(lst[midpoint:])
        R = mergesort(lst[:midpoint])
        return merge(L, R)
