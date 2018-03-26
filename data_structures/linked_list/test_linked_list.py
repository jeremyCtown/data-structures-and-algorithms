import pytest
from linked_list import LinkedList as LL

@pytest.fixture
def test_ll():
    return LL()
