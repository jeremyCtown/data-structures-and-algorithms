

# Inputs
old_list = [1, 2, 4, 5, 6]
new_element = 4

# New variables
counter = 0
new_list = []


def increment_counter():
    """
    Increments counter to equal list length
    """
    global counter
    for i in old_list:
        counter += 1
    print(counter)
    return counter


def new_counter():
    """
    Divides counter in half
    """
    global counter
    counter = counter/2
    print(counter)
    return counter


def insert_shift_array():
    """
    builds new list
    """
    global new_list
    for i in old_list:
        if old_list[i] < counter:
            new_list[i] == old_list[i]
        elif old_list[i] > counter and old_list[i] <= counter + 1:
            new_list[i] == new_element
        else:
            new_list[i] == old_list[i]
    return new_list


if __name__ == '__main__':
    increment_counter()
    new_counter()
    insert_shift_array()
