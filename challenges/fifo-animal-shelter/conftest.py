import pytest
from fifo_animal_shelter import AnimalShelter

@pytest.fixture
def empty_queue():
    return AnimalShelter()

@pytest.fixture
def small_queue():
    s= AnimalShelter()
    s.enqueue('cat')
    s.enqueue('dog')
    s.enqueue('dog')
    s.enqueue('cat')
    s.enqueue('dog')
    return s


@pytest.fixture
def dog_queue():
    s= AnimalShelter()
    s.enqueue('dog')
    s.enqueue('dog')
    s.enqueue('dog')
    s.enqueue('dog')
    s.enqueue('dog')
    return s

@pytest.fixture
def cat_queue():
    s= AnimalShelter()
    s.enqueue('cat')
    s.enqueue('cat')
    s.enqueue('cat')
    s.enqueue('cat')
    s.enqueue('cat')
    return s

