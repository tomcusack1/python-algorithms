def fib(n):
    # Using memoization we can improve this exponential fib algorithm from O(2^n) to O(N)
    # However, even memoization is overkill for this alg, when we only need to store the
    # data temporarily

    if n == 0:
        return 0

    a = 1
    b = 1
    i = 2

    while i < n:
        c = a + b
        a = b
        b = c
        i += 1

    return a + b

print fib(10)