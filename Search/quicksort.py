import unittest


def quick_sort(array: list) -> list:
    """An implementation of quick sort. """

    less = []
    equal = []
    greater = []

    if len(array) > 1:

        pivot = array[0]

        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        return list(quick_sort(less) + equal + quick_sort(greater))

    else:
        # Run out of recursive calls, return sorted list
        return array


class TestQuickSort(unittest.TestCase):
    def test(self):
        self.assertEqual(quick_sort([12, 4, 5, 6, 7, 3, 1, 15]), [1, 3, 4, 5, 6, 7, 12, 15])

if __name__ == '__main__':
    unittest.main()
