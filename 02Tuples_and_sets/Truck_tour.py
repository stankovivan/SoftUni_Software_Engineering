import copy
from collections import deque
lines = int(input())
total_fuel = 0
stops = 0
que = deque()

for _ in range(lines):
    que.append(input())
orig = copy.deepcopy(que)

while que:
    if stops == len(que):
        print(orig.index(que[0]))
        break

    for position in range(lines):
        fuel, distance = que[position].split()
        total_fuel += int(fuel)

        if total_fuel >= int(distance):
            total_fuel -= int(distance)
            stops += 1

        else:
            que.append(que.popleft())
            total_fuel = 0
            stops = 0
            break
