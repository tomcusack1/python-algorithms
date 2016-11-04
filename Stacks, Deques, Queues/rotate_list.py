def array_left_rotation(array, num_rotations):

    # Edge cases
    if not array:
        return []

    # Set up data structure
    stack = array
    i = 0

    print num_rotations

    # Do rotations
    while i < num_rotations:
        temp = stack.pop(0)
        stack.insert(len(stack), temp)
        i += 1

    return stack

# Get input
n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))

# Print output
answer = array_left_rotation(a, k)
print ' '.join(map(str, answer))
