n, m = map(int, input().split(" "))

z = n + m
counter = 0
first = set()
second = set()

for x in range(n):
    first.add(int(input()))
for x in range(m):
    second.add(int(input()))
for element in first & second:
    print(element)
