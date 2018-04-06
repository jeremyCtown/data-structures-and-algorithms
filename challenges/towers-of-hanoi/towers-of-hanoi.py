from stack import Stack


def towers_of_hanoi(n):
    """
    This is supposed to solve today's challenge... we'll see
    """

    A = Stack()
    B = Stack()
    C = Stack()

    for i in range(n, 0, -1):
        A.push(i)

    if A != C and B.top is None:
        C = A
    return "Disks moved from A to C"
