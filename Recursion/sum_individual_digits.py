def sum_individual_digits(n):

    if len(str(n)) == 1:
        # Base case
        return n
    else:
        return n % 10 + sum_individual_digits(n / 10)

print sum_individual_digits(4321)
