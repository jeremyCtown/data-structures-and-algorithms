import pytest
from ll_find_loop import LinkedList as LL


@pytest.fixture
def empty_ll():
    return LL()

@pytest.fixture
def single_ll():
    return LL([0])

@pytest.fixture
def small_ll():
    return LL([5, 6, 8, 9])

@pytest.fixture
def long_ll():
    return LL([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
