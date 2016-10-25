def triple_step(n):
    # A staircase of n steps can be hopped up 1 step, 2 steps or 3 steps at a time
    # This method counts how many possible ways one can go up the staircase starting on the first step

    # Using the algorithm: triple_step(n - 1) + (n - 2) + (n - 3)
    # has an exponential order, roughly O(3^n), since each call branches out three more calls

    # To solve this issue, I have memoised the algorithm to improve the efficiency

    # Edge cases
    if n < 0:
        return 0

    if n == 0:
        return 1

    return triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3)

print triple_step(3)
