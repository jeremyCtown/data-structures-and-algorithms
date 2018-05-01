# Hash Table

...and no, its not the thing your blown glass sits on

## Description

A hash table is a unique data structure that segments extremely large data sets into buckets, and nodes are then assigned to those buckets. This hash table uses linked lists to store those nodes.

## Setup
- [x] Create a new repository called hash_table and touch an __init__.py, README.md, hash_table.py, and test_hash_table.py

In hash_table.py:
- [x] Create a HashTable class, which when instantiated is aware of the following attributes:
    - max_size: defaults to 1024
    - buckets: defaults to a Python list()
    - This list structure should be instantiated with a size of max_size, where each element is a LinkedList

- [x] Define the following methods on your HashTable class:
    - hash_key: which accepts a string argument only, and returns a hashed value representing a single bucket location in your hash table
    - set: which accepts a key and value as arguments. The key will be used to as the hashed location for identifying a bucket. The value will be the actual data stored in the LinkedList as a new Node in that location.
    Note: This implies that your hash table will handle collisions using separate chaining.
    - get: which accepts a key and returns the value at that given key, using the key as an assumed value within the Node of the Linked List.
    - remove: which accepts a key and removes the given Node from the Linked List at that bucket.

You are welcome to modify this removal method to include functionality for removing the complete list, but this is not required.

### Resources

Scott's in-class demo