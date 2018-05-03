from hash_table import HashTable as hasher
import pytest

@pytest.fixture
def test_hasher():
    return hasher()
