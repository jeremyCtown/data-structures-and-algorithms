
def selection_smallest_first(lst):
    """Find smallest element and put it in index 0, sort from there."""
    for i in range(len(lst)):
        smallestIndex = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[smallestIndex]:
                smallestIndex = j
        if smallestIndex != i:
            lst[smallestIndex],lst[i] = lst[i],lst[smallestIndex]
    return lst


def selection_largest_first(lst):
    """Find largest element and move to end of list, sort from there."""
    for i in range(len(lst) - 1, 0, -1):
        max_val=0
        for j in range(1, i + 1):
            if lst[j] > lst[max_val]:
                max_val = j

        temp = lst[i]
        lst[i] = lst[max_val]
        lst[max_val] = temp

    return lst

