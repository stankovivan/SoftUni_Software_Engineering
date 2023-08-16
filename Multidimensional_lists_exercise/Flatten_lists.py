intro = input().split("|")

flaten = list()
for strings in intro[::-1]:
    flaten.extend(strings.split())
print(" ".join(flaten))
