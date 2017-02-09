import unittest


def odd_numbers(n: int) -> list:
    """This function returns a list of 20 odd numbers up from N

    For example:
        N = 1 --> [1, 3, 5, ... 39] (1-40)
        N = 2 --> [3, 5, 7, ... 41] (2-41)
        N = 3 --> [3, 5, 7, ... 41] (3-42)

    """
    try:
        if n % 2 is 0:
            return list(i for i in range(n+1, n+41, 2))
        else:
            return list(i for i in range(n, n+39, 2))

    except TypeError:
        return []


class TestOddNumbers(unittest.TestCase):
    def test_one(self):
        # Generates 20 odd numbers from 1-40
        result = odd_numbers(1)
        self.assertEqual(result, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])

    def test_two(self):
        # Generates 20 odd numbers from 2-41
        result = odd_numbers(2)
        self.assertEqual(result, [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41])

    def test_three(self):
        # Generates 20 odd numbers from 3-42
        result = odd_numbers(11)
        self.assertEqual(result, [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])

    def test_four(self):
        # Fails on type error. Float rather than int.
        result = odd_numbers(1.1)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
