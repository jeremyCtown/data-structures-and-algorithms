

# Inputs
search_list = [1, 2, 4, 5, 6]
new_integer = 3


def binary_search():
    """
    Increments counter to equal list length
    """
    counter = 0
    for i in search_list:
        counter = counter + 1
        if counter > len(search_list):
            print(int(-1))
            break
        if new_integer == search_list[i]:
            print(int(counter))
            break
        # elif counter == len(search_list):
        #     print(int(-1))
        #     break


binary_search()
