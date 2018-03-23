
# Inputs
counter = 0
new_list = [0]
answer = 0

test_list = [[1, 2], [2, 3], [3, 4], [4, 5]]


def sum_inner_lists():
    """
    sums inner lists from existing list and returns a new list
    """
    # new_list = [0]
    # counter = 0
    for i in test_list:
        print(i)
        i = (i[0]*i[1])
        return i


def largest_product(new_list):
    """
    loops through new_list and returns largest number
    """
    answer = 0
    for i in new_list:
        if answer < i:
            answer = i
    return answer


sum_inner_lists()
