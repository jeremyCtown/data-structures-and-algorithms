import pytest
from fifo_animal_shelter import AnimalShelter
from pets import Dog, Cat

@pytest.fixture
def empty_queue():
    return AnimalShelter()

@pytest.fixture
def small_queue():
    s= AnimalShelter()
    s.enqueue(Cat())
    s.enqueue(Dog())
    s.enqueue(Dog())
    s.enqueue(Cat())
    s.enqueue(Cat())
    return s


# @pytest.fixture
# def dog_queue():
#     s= AnimalShelter()
#     s.enqueue(Dog())
#     s.enqueue(Dog())
#     s.enqueue(Dog())
#     s.enqueue(Dog())
#     s.enqueue(Dog())
#     return s

# @pytest.fixture
# def cat_queue():
#     s= AnimalShelter()
#     s.enqueue(Cat())
#     s.enqueue(Cat())
#     s.enqueue(Cat())
#     s.enqueue(Cat())
#     s.enqueue(Cat())
#     return s

