def compress(s):
    """
    This compression algorithm uses the RunLength alg
    """

    r = ""
    l = len(s)
    count = 1
    i = 1

    # Edge case - Check if length 0
    if l == 0:
        return ""

    # Check if length 1
    if l == 1:
        return s + "1"

    while i < l:
        if s[i] == s[i - 1]:
            count += 1
        else:
            r = r + s[i - 1] + str(count)
            count = 1
        i += 1

    r = r + s[i - 1] + str(count)

    return r


print compress('AAABBBBZZZ')
