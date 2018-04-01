
# Inputs
test_list = [[1, 2], [2, 3], [3, 4], [4, 5]]

new_list = test_list


def create_new_list(test_list):
    """
    creates a new list from 2D array
    """
    counter = 0

    for items in test_list:
        print(test_list)
        for i in items:
            print(i)
            new_list[counter] = i
            print(new_list)
            counter = counter + 1
    # largest_product()
    print(new_list)


# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for row in a:
#     for elem in row:
#         print(elem)
#     print()


# def largest_product(new_list):
#     """
#     loops through new_list and returns product of two numbers largest number
#     """
#     answer = 0
#     for i in new_list:
#         for item in i:
#         product = new_list[i] * new_list[i+1]
#         print(product)
#         if answer < product:
#             answer = product
#     print(answer)
#     return answer


create_new_list(test_list)

# n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# # Add your function here

# def flatten(lists):
#   results = []
#   for numbers in lists:
#     for number in numbers:
#       results.append(number)
#   return results

# print flatten(n)
