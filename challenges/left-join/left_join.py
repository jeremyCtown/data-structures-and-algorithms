from repeated_word.hash_table import HashTable as ht

def left_join(left, right):

    for bucket in right.buckets:
        if right.bucket.key in left.buckets:
            left.buckets.key.value += ' ,{}'.format(right.bucket.key.value)
    return left




