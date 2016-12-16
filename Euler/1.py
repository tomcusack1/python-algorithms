def multiples(a0, d, n):
    nd = (n / d - 1) if n % d == 0 else n / d
    n_n_1 = (nd * (nd - 1)) / 2
    return a0 * nd + d * n_n_1

t = int(raw_input())
for a0 in xrange(t):
    n = int(raw_input())
    print multiples(3, 3, n) + multiples(5, 5, n) - multiples(15, 15, n)
