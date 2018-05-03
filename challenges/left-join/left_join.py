from ../hash_table/hash_table import HashTable as ht

def left_join(ht1, ht2):
    
    left = ht1
    right = ht2

    for bucket in right.buckets:
        if right.bucket.key in left.bucket:
            left.buckets.key += ' ,{}'.format(right.bucket.key.value)
    return left




