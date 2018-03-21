

# Inputs
search_list = [1, 2, 3, 5, 6]
new_integer = 4

# New variables
counter = 0


def binary_search():
    """
    Increments counter to equal list length
    """
    counter = 0
    for i in search_list:
        counter += 1
        if search_list[i] == new_integer:
            print(int(counter))
            break
    else:
        print(int(-1))


binary_search()
