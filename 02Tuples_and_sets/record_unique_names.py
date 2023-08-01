intro = int(input())
names_set = set()

for _ in range(intro):
    names = input()
    names_set.add(names)

for x in names_set:
    print(x)
