intro = input()
stack = list()
for index in range(len(intro)):
    char = intro[index]
    if char == "(":
        stack.append(index)
    elif char == ")":
        last = stack.pop()
        expresion = intro[last:index + 1]
        print(expresion)
