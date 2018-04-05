from stack import Stack
from node import Node as node


def multi_bracket_validation(stuff):
    """
    This is supposed to solve today's challenge... we'll see
    """

    answer = True
    checker = Stack()
    openers = ['[', '{', '(']
    # closers = [']', '}', ')']

    for i in stuff:
        if i in openers:
            checker.push(i)
        if i == ']':
            if checker.top.val != '[':
                answer = False
                break

    return answer
