from collections import deque
quantity_water = int(input())

opashka = deque()
while True:
    command = input()
    if command == "Start":
        break
    opashka.append(command)

while True:
    command = input()
    if command == "End":
        break
    doing = command.split()
    if len(doing) == 2:
        quantity_water += int(doing[1])
    else:
        person = opashka.popleft()
        liters = int(doing[0])

        if liters > quantity_water:
            print(f"{person} must wait")
        else:
            quantity_water -= liters
            print(f"{person} got water")

print(f"{quantity_water} liters left")