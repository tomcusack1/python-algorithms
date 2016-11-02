def countPairs(numbers, k):

    # Edge cases
    if not numbers:
        return 0

    H = set(numbers)
    ans = sum(1 for a in numbers if a - k in H)

    return ans

print countPairs([1, 1, 2, 2, 3, 3], 1)
