from collections import deque

chocolate = list(map(int, input().split(", ")))
cup_milk = deque(map(int, input().split(", ")))
milkshakes = 0

while milkshakes < 5 and chocolate and cup_milk:
    condition = False
    if chocolate[-1] <= 0:
        chocolate.pop()
        condition = True

    if cup_milk[0] <= 0:
        cup_milk.popleft()
        condition = True
    if condition:
        continue

    if chocolate[-1] == cup_milk[0]:
        milkshakes += 1
        chocolate.pop()
        cup_milk.popleft()
    else:
        cup_milk.append(cup_milk.popleft())
        chocolate[-1] -= 5

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

print(f"Chocolate: {', '.join(map(str, chocolate)) if chocolate else 'empty'}")
print(f"Milk: {', '.join(map(str, cup_milk)) if cup_milk else 'empty'}")
