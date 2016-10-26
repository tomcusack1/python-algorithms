def reverse(s):

    # Edge case
    if s == "":
        return ""

    # Base case (only one element left)
    if len(s) <= 1:
        return s

    # Recursion
    return reverse(s[1:]) + s[0]

print reverse("tom")
