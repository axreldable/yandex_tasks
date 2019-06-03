# check("{()}[]") // true
# check("{[}]") // false


def is_open(b):
    return b in ['{', '(', '[']


def is_pair(open, close):
    # print(open, close)
    return (open == '{' and close == '}') or \
           (open == '(' and close == ')') or \
           (open == '[' and close == ']')


def check(brackets):  # O(n)
    # brackets = list(brackets)
    stack = list()
    for b in list(brackets):
        if is_open(b):
            stack.append(b)
        else:
            if is_pair(stack.pop(), b) is not True:
                return False
    return True


print(check("{()}[]"))
print(check("{[}]"))
