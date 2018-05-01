from ../hash_table/hash_table import HashTable as ht

def repeated_word(string):
    new_string = string.split('')

    for word in new_string:
        ht.set()
        if word in ht:
            return word

