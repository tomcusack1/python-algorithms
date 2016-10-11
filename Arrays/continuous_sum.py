def large_cont_sum(arr):

    total = 0
    largest_num = []

    for i in arr:
        if i > 0:
            # Positive: Keep adding..
            total += i
        else:
            # We hit a negative number. Reset
            largest_num.append(total)
            total = 0

    largest_num.sort()
    return largest_num[-1]

print large_cont_sum([1, 2, -1, 3, 4, 10, 10, -1])