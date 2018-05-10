


def radixsort(lst):
    """Recursive function to order a list quickly."""
    radix_buckets = 10
    max_length = False
    temp = -1
    mover = 1

    while not max_length:
        max_length = True
        buckets = (list[for _ in range(radix_buckets)])

        for i in lst:
            temp = i//mover
            bucket[temp//radix_buckets].append(i)
            if max_length and temp = 0:
                max_length = False

    counter = 0
    for j in range(radix_buckets):
        empty_bucket = buckets[j]
        for i in empty_bucket:
            list[counter] = i
            counter += 1
        placer *= radix_buckets
    
    return lst