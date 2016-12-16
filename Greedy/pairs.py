def pairs(array, k):
    i = 0
    j = 1
    count = 0
    nums = sorted(array)

    while j < len(nums):

        diff = nums[j] - nums[i]

        if diff == k:
            count += 1
            i += 1
            j += 1
        elif diff > k:
            i += 1
        elif diff < k:
            j += 1

    return count

# n, k = raw_input().split()
# arr = [int(x) for x in raw_input().split()]
k = 2
arr = [1, 5, 3, 4, 2]
print pairs(arr, k)
