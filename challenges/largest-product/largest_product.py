
# Inputs
test_list = [[1, 2], [2, 3], [3, 4], [4, 5]]


def largest_product(test_list):
    """
    returns largest product of 2D array
    """
    answer = 0
    for i in range(len(test_list)):
        if len(test_list[i]) > 1 and test_list[i][0] * test_list[i][1] > answer:
            answer = test_list[i][0] * test_list[i][1]
        else:
            raise TypeError('Each index must contain a list with 2 values')
    return answer
