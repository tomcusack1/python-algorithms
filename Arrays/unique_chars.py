def unique_chars(s):
    chars = set()
    
    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)
    return True

sentence = "abc"
print unique_chars(sentence)
