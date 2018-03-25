
# Inputs
counter = 0
new_list = [0]
answer = 0

test_list = [[1, 2], [2, 3], [3, 4], [4, 5]]

class LargestProduct:
    """
    new class to complete challenge
    """
    def __init__(self, test_list):
        self.counter = 0
        self.answer = 0
        self.new_list = test_list
        self.test_list = test_list


    def multiply_inner_lists(self):
        """
        sums inner lists from existing list and returns a new list
        """
        for i in self.test_list:
            self.new_list[self.counter] = (i[0]*i[1])
            self.counter += 1
        self.largest_product()
        return self.new_list


    def largest_product(self):
        """
        loops through new_list and returns largest number
        """
        for i in self.new_list:
            if self.answer < i:
                self.answer = i
        return self.answer


if __name__ == '__main__':
    x = LargestProduct(test_list)
    x.multiply_inner_lists()
