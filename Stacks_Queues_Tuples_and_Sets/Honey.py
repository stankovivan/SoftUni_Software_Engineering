from collections import deque

bees = deque(map(int, input().split(" ")))
nectar = list(map(int, input().split(" ")))
command = deque(input().split(" "))
honey = 0

while bees and nectar:
    if nectar[-1] >= bees[0]:
        operators = command.popleft()
        collected, bee = nectar.pop(), bees.popleft()
        if operators == '+':
            honey += abs(bee + collected)
        elif operators == '-':
            honey += abs(bee - collected)
        elif operators == '*':
            honey += abs(bee * collected)
        elif operators == '/':
            if collected == 0 and bee == 0:
                continue
            honey += abs(bee / collected)
    else:
        nectar.pop()
print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
