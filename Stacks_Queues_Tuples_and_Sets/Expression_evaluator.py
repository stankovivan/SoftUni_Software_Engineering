from functools import reduce
intro = input().split(" ")
stack = []

for line in intro:
    if line == "+":
        stack = [reduce(lambda x, y: x + y, stack)]
    elif line == "-":
        stack = [reduce(lambda x, y: x - y, stack)]
    elif line == "*":
        stack = [reduce(lambda x, y: x * y, stack)]
    elif line == "/":
        stack = [reduce(lambda x, y: x // y, stack)]
    elif line.lstrip("-").isnumeric():
        stack.append(int(line))

print(stack[0])
