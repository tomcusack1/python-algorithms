# Q: Given N stacks. Each stack contains Si elements.
#    Find the max sum of M numbers in N stacks
#
# Ex: S = [1, 200, 1, 2, 3]
#     200 is max, but you must traverse 3, 2, 1 first.
#
# What is a better solution?


def sum_of_stacks(stacks):

    maximum_values = []

    for stack in stacks:
        maximum_values.append(find_max(stack))

    return sum(maximum_values)


def find_max(stack):
    is_maximum_value = 0

    for i in stack:
        if i > is_maximum_value:
            is_maximum_value = i

    return is_maximum_value

print sum_of_stacks([[1, 8, 100, 3], [2000, 2, 3, 1], [10, 1, 4]])
