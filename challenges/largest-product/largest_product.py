
# Inputs
test_list = [[1, 2], [2, 3], [3, 4], [4, 5]]


def multiply_inner_lists(test_list):
    """
    sums inner lists from existing list and returns a new list
    """
    counter = 0
    new_list = test_list
    for i in test_list:
        if len(i) > 1:
            new_list[counter] = (i[0]*i[1])
            counter += 1
        else:
            new_list[counter] = i[0]
            counter += 1
    largest_product(new_list)
    return new_list


def largest_product(new_list):
    """
    loops through new_list and returns largest number
    """
    answer = 0
    for i in new_list:
        product = i * (i+1)
        print(product)
        if answer < product:
            answer = product
    print(answer)
    return answer

multiply_inner_lists(test_list)
