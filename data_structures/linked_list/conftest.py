import pytest
from linked_list import LinkedList as LL


@pytest.fixture
def test_ll():
    return LL()


@pytest.fixture
def short_ll():
    return LL([1, 2, 3, 4])
