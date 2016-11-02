def braces(s):
    global_string = ""

def balance_check(s):

    # Edge case check
    if len(s) % 2 != 0:
        return False

    # Set up the strings to check or
    opening = set('({[')
    matches = set([ ('(', ')'), ('[', ']'), ('{', '}') ])
    stack = []

    for parenthesis in s:
        if parenthesis in opening:
            stack.append(parenthesis)
        else:
            if len(stack) == 0:
                return False

            # Remove items from the stack
            last_open = stack.pop()

            if (last_open, parenthesis) not in matches:
                return False

    return len(stack) == 0

balance_check('[]')
