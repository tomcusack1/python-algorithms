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
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    # Edge case check
    if len(str1) != len(str2):
        # There are differing numbers of letters
        return False

    count = {}

    for letter in str1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in str2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True

print anagram('abc', 'abc')
