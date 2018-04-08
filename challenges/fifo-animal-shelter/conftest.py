import pytest
from fifo_animal_shelter import AnimalShelter
from pets import Dog, Cat

@pytest.fixture
def empty_queue():
    """
    Creates empty queue
    """
    return AnimalShelter()

@pytest.fixture
def small_queue():
    """
    Populates queue with nodes
    """
    s= AnimalShelter()
    s.enqueue(Cat())
    s.enqueue(Dog())
    s.enqueue(Dog())
    s.enqueue(Cat())
    s.enqueue(Cat())
    return s

