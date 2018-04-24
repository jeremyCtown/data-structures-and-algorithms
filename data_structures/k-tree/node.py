
class Node(object):
    def __init__(self, val):
        self._val = val
        self.children = []

    
    def __repr__(self):
        return 'Val: {0} Children: {1}'.format(self.value, self.children)


    def add_child(self, obj):
        self.children.append(obj)