lines = int(input())
unique = set()

for _ in range(lines):
    chemical_compounds = input().split(" ")

    for element in chemical_compounds:
            unique.add(element)

for el in unique:
    print(el)
