class Palindrome:

    @staticmethod
    def is_palindrome(word):

        # Edge case check
        if word == "":
            return False

        word_list = list(word.lower())
        reversed_word = []

        # Reverse word_list into new list
        for letter in word_list:
            reversed_word.insert(0, letter)

        # Compare the two strings
        if word_list == reversed_word:
            return True

        return False

print Palindrome.is_palindrome('Aba')
