import pytest
from queue import Queue

@pytest.fixture
def empty_queue():
    return Queue()

@pytest.fixture
def small_queue():
    s= Queue()
    s.enqueue(4)
    s.enqueue(5)
    s.enqueue(6)
    s.enqueue(7)
    s.enqueue(8)
    return s

@pytest.fixture
def large_queue():
    s = Queue()

    for num in range(1000):
        s.enqueue(num)

    return s

@pytest.fixture
def iter_queue():
    return Queue([7, 8, 9])

