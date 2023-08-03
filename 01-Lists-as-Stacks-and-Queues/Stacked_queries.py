from collections import deque
intro = int(input())
stack = deque()

for x in range(intro):
    queries = input().split(" ")

    if int(queries[0]) == 1:
        number = queries[1]
        stack.append(number)
    elif int(queries[0]) == 2:
        if len(stack) == 0:
            continue
        stack.pop()
    elif int(queries[0]) == 3:
        if len(stack) == 0:
            continue
        print(max(stack))
    elif int(queries[0]) == 4:
        if len(stack) == 0:
            continue
        print(min(stack))

print(", ".join(reversed(stack)))
