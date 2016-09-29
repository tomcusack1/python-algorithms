def anagram(str1, str2):
    '''
    Anagram function accepts two strings
    and returns true/false if they are
    valid anagrams of one another
    e.g. 'dog' and 'god' = true

    :string str1:
    :string str2:
    :return: boolean
    '''
    sorted_str1 = quicksort(str1)
    sorted_str2 = quicksort(str2)
    if (sorted_str1 == sorted_str2):
        return True
    return False

def quicksort(lst):
    '''
    Sorts string values
    :param string:
    :return: string:
    '''

    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))

print anagram('abc', 'abb')  # Returns false
