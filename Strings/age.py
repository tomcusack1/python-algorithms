import unittest


class Age(object):
    """The age of a person is stored in this class.

        Attributes:
            age (int): The age of a person

        """
    def __init__(self, age: int):
        self.age = age

    def guess_age(self, guess: int) -> bool:
        """A method which returns whether the age was correct or not"""
        try:
            if guess is self.age:
                return True
            return False

        except TypeError:
            Exception("Donald's age can only be an integer.")

donald = Age(20)


class TestGuessAge(unittest.TestCase):
    def test_false(self):
        for i in range(5):
            self.assertEqual(donald.guess_age(i), False)

    def test_true(self):
        self.assertEqual(donald.guess_age(20), True)

    def test_data_type(self):
        self.assertEqual(donald.guess_age(21.5), False)

if __name__ == '__main__':
    unittest.main()
