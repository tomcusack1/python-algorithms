from string import ascii_lowercase


def pangram(sentence):
    # Construct an alphabet list
    alphabet = list(ascii_lowercase)
    s = set(sorted(sentence.replace(' ', '')))

    if ''.join(sorted(alphabet)) == ''.join(sorted(s)):
        return 'pangram'
    else:
        return 'not pangram'

print pangram(raw_input().lower().strip())
#print pangram('We promptly judged antique ivory buckles for the next prize'.lower())
