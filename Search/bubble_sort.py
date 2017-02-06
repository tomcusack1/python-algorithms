import unittest

def bubble_sort(array):
    """
        Implementation of Bubble Sort.
    """
    for n in range(len(array) -1, 0, -1):
        for k in range(n):
            if array[k] > array[k+1]:
                temp = array[k]
                array[k] = array[k+1]
                array[k+1] = temp
    return array

class TestBubbleSort(unittest.TestCase):
    def test_one(self):
        result = bubble_sort([3, 2, 1])
        self.assertEqual(result, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
