def change_making_problem(target, coins, known_results):

    # Minimum number of coins for change

    # Default value set to target
    min_coins = target

    # Base case
    if target in coins:
        # 1 coin, because there is a coin in
        # our coins list that covers our change
        # I.e. (10, [10]), we can give a 10p coin straight away
        known_results[target] = 1
        return 1

    elif known_results[target] > 0:
        return known_results[target]

    else:
        # For every coin value in that coins list
        # that is <= the target. Recursively call
        # change_making_problem(), and add a count coin
        # and subtract from the target. Then reset the minimum
        # if we have a new minimum number of coins
        for i in [c for c in coins if c <= target]:

            # Add a coin count + recurse
            # e.g. Looking for 15p, subtract 10p, target = 5p
            num_coins = 1 + change_making_problem(target - i, coins, known_results)

            # Reset if the new num_coins is less than min_coins
            if num_coins < min_coins:
                min_coins = num_coins

                # Reset known results
                known_results[target] = min_coins

    return min_coins

target = 74
x = [0] * (target + 1)
print change_making_problem(target, [1, 5, 10, 25], x)
