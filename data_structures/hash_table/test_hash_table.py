from hash_table import HashTable as hasher
import pytest


def test_max_size_is_1024(test_hasher):
    """Check max size is 1024 and create 1024 buckets."""
    assert test_hasher.max_size == 1024
    assert len(test_hasher.buckets) == 1024


def test_size_not_greater_than_024(test_hasher):
    """Check max size cannot be greater than 1024"""
    assert test_hasher.max_size != 1025


def test_hash_table_max_size_can_change():
    """Test max size can be changed."""
    hashed = hasher(1200)
    assert hashed.max_size == 1200
    assert len(hashed.buckets) == 1200


def test_hash_table_buckets_are_LL(test_hasher):
    """Test buckets are linked lists."""
    assert test_hasher.buckets[0].__doc__ == "This is a Linked List"


def test_hash_key_method_raise_error_for_int(test_hasher):
    """Test hash key does not accept ints"""
    with pytest.raises(TypeError):
        test_hasher.hash_key(5)


def test_hash_key_method_raise_error_for_float(test_hasher):
    """Test hash key does not accept floats"""
    with pytest.raises(TypeError):
        test_hasher.hash_key(5.67)


def test_hash_key_method_raise_error_for_lists(test_hasher):
    """Test hash key does not accept lists"""
    with pytest.raises(TypeError):
        test_hasher.hash_key(['green', 'red', 'blue'])


def test_hash_key_method_creates_hash_key(test_hasher):
    """Test hash key accepts string."""
    assert test_hasher.hash_key('c') == 99


def test_string_creates_hash_key(test_hasher):
    """Test hash key hashes word."""
    assert test_hasher.hash_key('cat') == 312


def test_set_creates_node(test_hasher):
    """Test set creates a record in hash table."""
    test_hasher.set('cat', 'dog')
    assert test_hasher.buckets[312].head.val['cat'] == 'dog'


def test_set_collisions_create_multiple_records(test_hasher):
    """Test collisions create separate records."""
    test_hasher.set('cat', 'dog')
    test_hasher.set('act', 'out')
    assert test_hasher.buckets[312].head.val['act'] == 'out'
    assert test_hasher.buckets[312].head._next.val['cat'] == 'dog'
    assert test_hasher.buckets[312]._size == 2


def test_set_accepts_dicts(test_hasher):
    """Test set allows for dicts as values in hash table."""
    test_hasher.set('wtf', {'watup':'dude'})
    assert test_hasher.hash_key('wtf') == 337
    assert test_hasher.buckets[337].head.val['wtf'] == {'watup':'dude'}


def test_set_accepts_dicts(test_hasher):
    """Test set allows for integers as values in hash table."""
    test_hasher.set('over', 9000)
    assert test_hasher.hash_key('over') == 444
    assert test_hasher.buckets[444].head.val['over'] == 9000
    

def test_get_gets_things(test_hasher):
    """Test get returns key/value pair."""
    test_hasher.set('wtf', {'watup':'dude'})
    assert test_hasher.get('wtf') == [{'watup':'dude'}]


def test_one_key_gets_multiple_things(test_hasher):
    """Test get returns key/value pair."""
    test_hasher.set('wtf', 'dude')
    test_hasher.set('wtf', 'watup')
    assert test_hasher.get('wtf') == ['watup','dude']


def test_key_does_not_get_other_things(test_hasher):
    """Test key does not return all the things."""
    test_hasher.set('wtf', 'dude')
    test_hasher.set('wtf', 'watup')
    test_hasher.set('woot', 'wtf')
    assert test_hasher.get('wtf') != 'wtf'


def test_remove_pulls_key_value_single_record(test_hasher):
    """Test remove method removes node at key."""
    test_hasher.set('dude', 'is chill')
    assert test_hasher._size == 1
    assert test_hasher.remove('dude').val == {'dude': 'is chill'} 
    assert test_hasher._size == 0


def test_remove_pulls_key_value_from_multiple_records(test_hasher):
    """Test remove method removes node at key."""
    test_hasher.set('wtf', 'watup')
    test_hasher.set('woot', 'wtf')
    test_hasher.set('dude', 'is chill')
    assert test_hasher.remove('woot').val == {'woot': 'wtf'} 


def test_remove_false_key_raises_error(test_hasher):
    """Test remove method reduces number of records."""
    test_hasher.set('dude', 'is chill')
    with pytest.raises(ValueError):
        test_hasher.remove('woot')


def test_remove_actually_removes_key(test_hasher):
    """Test remove method reduces number of records."""
    test_hasher.set('dude', 'is chill')
    assert test_hasher.remove('dude').val == {'dude': 'is chill'}
    assert test_hasher._size == 0
    with pytest.raises(ValueError):
        test_hasher.remove('dude')





