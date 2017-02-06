def sequential_search(array: list, element: int) -> bool:
    """
    General sequential search. Works on ordered lists only
    """
    for item in array:
        if item == element:
            return True
        if item > element:
            return False

    return False

print(sequential_search([1, 2, 3], 4))
