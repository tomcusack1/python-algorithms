from collections import defaultdict

def most_frequent(arr):

    # Edge cases
    if not arr:
        # Passed an empty array
        return 0

    if len(arr) == 1:
        return arr

    # Set up our default dictionary to store the count of the ints
    count = defaultdict(int)

    # Count the occurrences of a number
    for number in arr:
        count[number] += 1

    i = 0
    most_frequent_number = 0
    while i < len(count):
        # Iterate over the dictionary
        print count[arr[i]]
        i += 1

    return count

print most_frequent([2, 2, 2, 3, 3, 4])
