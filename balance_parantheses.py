def balance_check(s):
    if len(s) % 2 != 0:
        return False

    opening = set('([{')
    matches = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if not (last_open, paren) == (last_open, matches[last_open]):
                return False

    return len(stack) == 0

print(balance_check('[()]{[[[[]]]]}'))
