from collections import deque

toys = {
    'Doll': {
        'magic': 150,
        'crafted': 0
    },
    'Wooden train': {
        'magic': 250,
        'crafted': 0
    },
    'Teddy bear': {
        'magic': 300,
        'crafted': 0
    },
    'Bicycle': {
        'magic': 400,
        'crafted': 0
    }

}

materials = list(map(int, input().split(" ")))
magic = deque(map(int, input().split()))
dsa = []

while magic and materials:
    total_magic = 0
    condition = False
    if materials[-1] == 0:
        materials.pop()
        condition = True
    if magic[0] == 0:
        magic.popleft()
        condition = True
    if condition:
        continue
    product = materials[-1] * magic[0]
    if product == toys["Doll"]["magic"]:
        toys["Doll"]["crafted"] += 1
        materials.pop()
        magic.popleft()
    elif product == toys["Wooden train"]["magic"]:
        toys["Wooden train"]["crafted"] += 1
        materials.pop()
        magic.popleft()
    elif product == toys["Teddy bear"]["magic"]:
        toys["Teddy bear"]["crafted"] += 1
        materials.pop()
        magic.popleft()
    elif product == toys["Bicycle"]["magic"]:
        toys["Bicycle"]["crafted"] += 1
        materials.pop()
        magic.popleft()
    else:
        if product > 0:
            materials[-1] += 15
            magic.popleft()
        elif product < 0:
            materials.append(materials.pop() + magic.popleft())

if toys["Doll"]["crafted"] > 0 and toys["Wooden train"]["crafted"] > 0 or toys["Teddy bear"]["crafted"] > 0 and \
        toys["Bicycle"]["crafted"] > 0:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    final = ''

    for n in range(len(materials)):
        dsa.append(str(materials.pop()))
    print(f"Materials left: {', '.join(dsa)}")

if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for t in sorted(toys):
    if toys[t]['crafted'] > 0:
        print(f"{t}: {toys[t]['crafted']}")
