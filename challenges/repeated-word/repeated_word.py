from hash_table import HashTable as ht

def repeated_word(string):
    """Return the first word to appear twice in a string."""
    new_string = string.split()
    table = ht()

    for word in new_string:
        check_word = table.get(word)
        if check_word is not None:
            return word
        table.set(word, 1)

