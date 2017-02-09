import unittest


def sequential_search(array: list, element: int) -> bool:
    """
    General sequential search. Works on ordered lists only
    """
    for item in array:
        if item == element:
            return True
        if item > element:
            return False

    return False


class TestSearch(unittest.TestCase):
    def test_false(self):
        result = sequential_search([1, 2, 3], 4)
        self.assertEqual(result, False)

    def test_true(self):
        result = sequential_search([1, 2, 3], 3)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()