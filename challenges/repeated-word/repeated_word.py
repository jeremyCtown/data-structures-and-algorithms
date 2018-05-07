from .data_structures/hash_table/hash_table import HashTable as ht

def repeated_word(string):
    """Return the first word to appear twice in a string."""
    new_string = string.split('')

    for word in new_string:
        check_word = ht.get(word)
        if check_word is not None:
            return word
        ht.set(word, 1)

