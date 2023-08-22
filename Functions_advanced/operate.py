def operate(operator, *args):
    result = 0
    res = 1
    if operator == "+":
        for numbers in args:
            result += numbers
        return result

    if operator == "-":
        for numbers in args:
            result -= numbers
        return result
    if operator == "*":
        for numbers in args:
            res *= numbers
        return res
    if operator == "/":
        for numbers in args:
            des = None
            res /= numbers
            des /= numbers
        return des

print(operate("/", 120, 6))

