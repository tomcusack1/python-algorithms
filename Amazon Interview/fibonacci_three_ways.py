import nose
import timeit


def fib_recursive(n):
    # Base cases
    if n == 0 or n == 1:
        return n
    # Recursive case
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_dynamic(n):

    # Cache
    cache = [None] * (n + 1)

    # Base cases
    if n == 0 or n == 1:
        return n

    # Check cache
    if cache[n] != None:
        return cache[n]

    cache[n] = fib_dynamic(n - 1) + fib_dynamic(n - 2)

    return cache[n]


def fib_iterative(n):
    # Iteratively constructing the Fib method
    a, b = 0, 1

    for i in xrange(n):
        a, b = b, a + b

    return a

start_time = timeit.default_timer()
fib_recursive(10) # 5.5ms
print(float(timeit.default_timer() - start_time))

start_time = timeit.default_timer()
fib_dynamic(10) # FASTEST: 5ms
print(float(timeit.default_timer() - start_time))


start_time = timeit.default_timer()
fib_iterative(10) # 7ms
print(float(timeit.default_timer() - start_time))
