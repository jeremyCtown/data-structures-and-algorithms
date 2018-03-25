

# Inputs
test_list = [1, 2, 4, 5, 6]
test_num = 3


class ShiftArray:
    """
    new class to complete challenge
    """
    def __init__(self, test_list, test_num):
        self.counter = 0
        self.new_list = ['']

    def increment_counter(self, test_list):
        """
        Increments counter to equal list length
        """
        for i in test_list:
            self.counter += 1
        print(self.counter)
        return int(self.counter)


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
    for i in test_list:
        if test_list[i] < counter:
            new_list[i] == test_list[i]
        elif test_list[i] > counter and test_list[i] <= counter + 1:
            new_list[i] == new_element
        else:
            new_list[i] == test_list[i]
    return new_list


if __name__ == '__main__':
    x = ShiftArray(test_list, test_num)
    x.increment_counter()
    new_counter()
    insert_shift_array()
