import unittest

def binary_search(array: list, element: int):
    """
    Recursive implementation of a binary search. List must be sorted.
    """

    # Base case
    if len(array) == 0:
        return False
    else:

        middle = int(len(array) / 2)

        if array[middle] == element:
            # Found the element in the middle of the list
            found = True
        else:
            if element < array[middle]:
                # Search in the bottom half of the list
                return binary_search(array[:middle], element)
            else:
                # Search in the top half
                return binary_search(array[middle+1:], element)
    return True

class TestBinarySearch(unittest.TestCase):
    def test_one(self):
        result = binary_search([1, 2, 3], 1)
        self.assertEqual(result, True)

    def test_two(self):
        result = binary_search([2, 4, 6, 7, 11], 5)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
