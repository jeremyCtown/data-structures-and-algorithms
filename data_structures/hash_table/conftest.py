import pytest
from .hash_table import HashTable


@pytest.fixture
def test_hash():
    """Empty hash table."""
    return HashTable()
