import collections

def finder(arr1, arr2):
    # Perform an XOR between the numbers in the arrays
    result = 0
    for num in arr1 + arr2:
        result ^= num
    return result

# Arr2 is shuffled, then one element is popped
# randomly. Finder() finds this element
arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [1, 2, 3, 4, 5, 6]
print finder(arr1, arr2)
