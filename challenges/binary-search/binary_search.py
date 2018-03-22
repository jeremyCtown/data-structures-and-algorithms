

# Inputs
search_list = [1, 2, 4, 5, 6]
new_integer = 4


def binary_search():
    """
    Increments counter to equal list length
    """
    counter = 0
    for i in search_list:
        counter = counter + 1
        if new_integer == i:
            print(int(counter-1))
            break
    else:
        print(-1)


binary_search()
