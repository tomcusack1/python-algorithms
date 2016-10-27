def permute(s):

    out = []

    # Base case: One letter left
    if len(s) == 1:
        out = [s]

    else:
        # For every letter in the string
        for i, let in enumerate(s):
            # For every permutation resulting from step 2 and 3
            for perm in permute(s[:i] + s[i+1:]):
                # Getting everything up to the index
                # and attaching it to the index + 1 all the way to the end

                # print 'Current letter is: ', let
                # print 'Perm is', perm
                out += [let + perm]
                # print 'New permutation is: ', out

    return out

print permute('cusack')
