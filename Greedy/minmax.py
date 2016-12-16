def min_max(arr):

    # Edge case
    if len(arr) < 2:
        raise Exception('You need more than 1 element in the array to check')

    closest = []

    for number in arr[1:]:
        print number

    return closest

n = int(raw_input())
k = int(raw_input())
array = [int(raw_input()) for _ in xrange(0, n)]

print min_max(array)
