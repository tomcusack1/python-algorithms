from collections import defaultdict


def bits(n):
    n += 2**32
    return bin(n)[-32:]

k1 = bits(hash('Thomas'))
k2 = bits(hash('Tom'))
diff = ('^ ' [a == b] for a, b in zip(k1, k2))
print k1; print k2; print ''.join(diff)

dictionary = defaultdict(int)
words = ['tom', 'tom', 'tom']

for word in words:
    dictionary[word] += 1

print dictionary['tom']
