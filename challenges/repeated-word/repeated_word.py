from hash_table import HashTable as ht

def repeated_word(string):
    """Return the first word to appear twice in a string."""
    new_string = string.split()
    table = ht()

    if len(new_string) < 1:
        return 'Empty string'

    for word in new_string:
        check_word = table.get(word)
        if len(check_word) == 1:
            return word
        table.set(word, 1)
    
    return 'No words repeat'

