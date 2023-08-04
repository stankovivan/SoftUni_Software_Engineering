intro = input()

elements_dick = dict()

for char in intro:

    if char in elements_dick.keys():
        elements_dick[char] += 1
    else:
        elements_dick[char] = 1

for i in sorted(elements_dick.keys()):
    print(f"{i}: {elements_dick[i]} time/s")
