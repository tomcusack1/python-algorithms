def number(n):

    # Create cache
    cache = [None] * (n + 1)

    # Base case
    if n == 0 or n == 1:
        return n

    # Edge case
    if n < 0:
        return 0

    # Check cache
    if cache[n] is not None:
        return cache[n]

    cache[n] = number(n / 2)

    return cache[n]

print number(12)
