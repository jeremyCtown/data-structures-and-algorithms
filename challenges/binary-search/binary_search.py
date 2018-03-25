
# Inputs
test_list = [1, 2, 4, 5, 6]
test_num = 4


class BinarySearch:
    """
    new class to complete challenge
    """
    def __init__(self, test_list, test_num):
        self.counter = 0
        self.test_list = test_list
        self.test_num = test_num
        self.answer = 0

    def binary_search(self, test_list, test_num):
        """
        Increments counter to equal list length
        """
        for i in self.test_list:
            self.counter = self.counter + 1
            if self.test_num == i:
                self.answer = int(self.counter-1)
                # print(self.answer)
                # return(self.answer)
                # # break
        else:
            self.answer = -1
        return(self.answer)


if __name__ == '__main__':
    x = BinarySearch(test_list, test_num)
    x.binary_search()
