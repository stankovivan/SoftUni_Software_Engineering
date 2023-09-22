class Value_cannotBeNegative(Exception):
    """'ne stava"""
    pass


num = list()
for i in range(5):
    number = int(input())
    if number < 0:
        raise Value_cannotBeNegative

    else:
        num.append(number)

print(num)
