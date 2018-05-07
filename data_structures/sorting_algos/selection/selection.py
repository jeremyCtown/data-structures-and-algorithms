
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


# def selection(lst):

#     for i in range(len(lst)):
#         min_i = min(lst[i:]) #find maximum element
#         min_index = lst[i:].index(min_i) #find index of maximum element
#         lst[i + min_index] = lst[i] #replace element at min_index with first element
#         lst[i] = min_i                 #replace first element with min element
#     return lst


# def selection(lst):
#     """
#     Find the smallest element in the list and put it (swap it) in the first location, 
#     Find the second element and put it (swap it) in the second locaiton, and so on. 
#     """
#     for i in range(len(lst) - 1):
#         minIndx = i
#         minVal= lst[i]
#         j = i + 1
#         while j < len(lst):
#             if minVal > lst[j]:
#                 minIndx = j
#                 minVal= lst[j]
#             j += 1
#         temp = lst[i]
#         lst[i] = lst[minIndx]
#         lst[minIndx] = temp 
#     return lst
