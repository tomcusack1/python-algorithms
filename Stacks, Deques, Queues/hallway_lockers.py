def min_max(n):

    sums = []

    for i in n:
        total = 0
        for j in n:
            if j is not i:
                total += j
        sums.append(total)

    return str(min(sums)) + " " + str(max(sums))

array = [long(i) for i in raw_input().split()]

print min_max(array)
