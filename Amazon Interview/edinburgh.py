def solution(arr):

    count = 0
    a = 0
    b = 0
    i = -1

    while i < len(arr):
        a = arr[i]
        b = arr[i + 1]
        print a
        print b
        i += 1
    return count

print solution([1, 2, -1, 3, 4, 10, 10, -1])