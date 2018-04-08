from towers_of_hanoi import towers_of_hanoi

stuff = 1
more_stuff = 3
lotsa_stuff = 999


def test_1(stuff):
    """ Testing for stuff """
    assert towers_of_hanoi.A.size == 1


def test_2(more_stuff):
    """ Testing more stuff """
    assert towers_of_hanoi.C.size == 3


def test_3(lotsa_stuff):
    """ Apparently more stuff to test """
    assert towers_of_hanoi.B.head is None

