test_list = [3, 4, 5, 7, 8, 9]
test_num = 6


class ShiftArray:
    """
    new class to complete challenge
    """
    def __init__(self, test_list, test_num):
        self.counter = 0
        self.zero = 0
        self.new_list = test_list + [0]
        self.insert_index = 0
        self.splitter = 0
        self.test_list = test_list
        self.test_num = test_num

    def increment_counter(self):
        """
        Increments counter to equal list length
        """
        for i in self.test_list:
            self.counter += 1
            self.splitter = self.counter
        self.split_counter(self.splitter)
        return self.counter

    def split_counter(self, splitter):
        """
        Divides counter in half
        """
        self.insert_index = float(splitter)/2
        self.insert_shift_array(self.test_list, self.test_num, self.insert_index)
        return self.insert_index

    def insert_shift_array(self, test_list, test_num, splitter):
        """
        builds new list
        """

        for i in test_list:
            if self.zero < splitter:
                self.new_list[self.zero] = i
                self.zero += 1
            elif (splitter + 1) > self.zero >= splitter:
                self.new_list[self.zero] = test_num
                self.new_list[self.zero + 1] = i
                self.zero += 2
            else:
                self.new_list[self.zero] = i
                self.zero += 1
        print(self.new_list)
        return(self.new_list)


if __name__ == '__main__':
    x = ShiftArray(test_list, test_num)
    x.increment_counter()
