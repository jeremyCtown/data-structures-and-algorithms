from node import Node


class LinkedList:
    """
    Doc strings are gud
    """
    def __init__(self, iter=[]):
        self.head = None
        self._size = 0
        self._current = self.head

        for item in reversed(iter):
            self.insert(item)

    def __repr__(self):
        """
        assumes head will have a val and we will need this
        """
        return '<head> => {}'.format(self.head.val)

    def __str__(self):
        """ this is where we can see the list"""

    def __len__(self):
        """
        returns size of LL
        """
        return self._size

    def insert(self, val):
        """
        basic insertion method for adding to front of LL
        """
        self.head = Node(val, self.head)
        self._size += 1

    def append(self, val):
        """
        appends node to the end of the LL
        """
        new_node = Node(val, None)
        current = self.head._next
        while current._next is not None:
            current._next = current._next._next
            if current._next._next is None:
                current._next._next = new_node
                new_node._next is None
                self._size += 1
                return new_node._next

    def find(self, val):
        """
        Searches through a list for val and returns the node with that val
        """

        current = self.head
        while current:
            if val == current.val:
                return True

            current = current._next
        return False

    def insert_before(self, val, new_val):
        """
        inserts node before node at val
        """
        new_node = Node(new_val)
        current = self.head._next
        while current._next is not None:
            if current._next.val == val:
                new_node._next = current._next
                current._next = new_node
                self._size += 1
                break

            current = current._next

        if current._next is None:
            raise ValueError("Data not in list")

    def insert_after(self, val, new_val):
        """
        inserts node after node at val
        """
        new_node = Node(new_val)
        current = self.head._next
        while current._next is not None:
            if current.val == val:
                new_node._next = current._next._next
                current._next = new_node
                self._size += 1
                break

            current = current._next

        if current._next is None:
            raise ValueError("Data not in list")

    def kth_from_end(self, k):
        """
        returns node at kth from end
        """
        current = self.head
        counter = 0
        answer = 0
        kth = self._size - k
        while current._next is not None:
            if counter == kth:
                answer = current
                break
            else:
                counter += 1
                current = current._next
        return answer

    def has_loop(self):
        """
        checks if LL has a loop
        """

        current = self.head
        fast = self.head

        if current is None:
            return False

        while current._next is not None:
            fast = fast._next
            slow = current
            if fast is None:
                return False
            if fast is slow:
                return True
            # else:
            #     fast = current._next._next
            #     print('next')
        else:
            return False


def merge_lists(ll_1, ll_2):
    """
    merges two lists
    """
    baselist = 0
    zipped = 0

    if (ll_1._size >= ll_2._size):
        baselist = ll_1
        zipped = ll_2
    else:
        baselist = ll_2
        zipped = ll_1

    if zipped.head is None:
        return baselist.head

    current = baselist.head
    temp = current._next
    zipped = zipped.head
    while current._next is not None:
        current._next = zipped
        current = current._next
        current._next = temp
        temp = temp._next
        current = current._next
        zipped = zipped._next
    return baselist.head



