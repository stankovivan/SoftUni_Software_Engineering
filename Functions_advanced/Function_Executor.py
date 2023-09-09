def func_executor(*args):
    result = ''
    for fun in args:
        result += f'{fun[0].__name__} - {fun[0](*fun[1])}' + "\n"
    return result


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))
