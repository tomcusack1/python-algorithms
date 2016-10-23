def recursive_sum(n):
    # Base check
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)

print recursive_sum(4)
