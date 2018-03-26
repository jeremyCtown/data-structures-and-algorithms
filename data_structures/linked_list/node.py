
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return '{data}'.format(val=self.data)

    def __str__(self):
        return '{data}'.format(val=self.data)

    def get_data(self):
        return self.data

