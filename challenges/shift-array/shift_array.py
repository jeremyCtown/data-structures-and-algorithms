

# Inputs
test_list = [1, 2, 4, 5, 6]
test_num = 3


class ShiftArray:
    """
    new class to complete challenge
    """
    def __init__(self, test_list, test_num):
        self.counter = 0
        self.zero = 0
        self.new_list = ['']
        self.insert_index = 0

    def increment_counter(self, test_list):
        """
        Increments counter to equal list length
        """
        for i in test_list:
            self.counter += 1
            self.splitter = self.counter
        self.split_counter(self.splitter)
        return self.counter

    def split_counter(self, splitter):
        """
        Divides counter in half
        """
        self.insert_index = splitter/2
        self.insert_shift_array(test_list, test_num, self.insert_index)

    def insert_shift_array(self, test_list, test_num, splitter):
        """
        builds new list
        """
        for i in test_list:
            if self.zero <= splitter:
                self.new_list[self.zero] = test_list[self.zero]
                self.zero += 1
        return self.new_list
                # return self.zero
        #         self.new_list[self.zero] == i
        #         self.zero += 1
        # return self.new_list
        #     elif test_list[i] > self.counter and test_list[i] <= self.counter + 1:
        #         self.new_list[i] == test_num
        #     else:
        #         self.new_list[i] == test_list[i]
        # return self.new_list


if __name__ == '__main__':
    x = ShiftArray(test_list, test_num)
    x.increment_counter()
    # new_counter()
    # insert_shift_array()
