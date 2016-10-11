def pair_sum(arr, k):

    # Edge case check
    if len(arr) < 2:
        print "CRITICAL: You need to pass 2 or more elements into pair_sum"
        return

    # Sets for tracking
    seen = set()
    output = set()

    for num in arr:

        target = k - num  # Get difference

        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num, target)), max(num, target)))

    print '\n'.join(map(str, list(output)))

pair_sum([1, 3, 2, 2], 4)
