from collections import deque
intro = input().split(" ")

final = deque()

for x in range(len(intro)):
    final.append(intro.pop())

print(" ".join(final))
