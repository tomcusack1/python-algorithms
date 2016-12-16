def fib(n):
    a, b = 0, 1
    total = 0
    for i in xrange(n):
        if b > n:
            return total
        else:
            a, b = b, a + b
            if a % 2 == 0:
                if a > n:
                    return total
                else:
                    total += a
    return total

t = int(raw_input())
for i in xrange(t):
    print fib(long(raw_input()))
