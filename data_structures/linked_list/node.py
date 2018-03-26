
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '{data}'.format(val=self.data)

    def __str__(self):
        return '{data}'.format(val=self.data)
