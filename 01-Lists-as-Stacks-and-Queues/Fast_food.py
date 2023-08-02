from collections import deque
quantity_of_food = int(input())
order = deque(map(int, input().split(" ")))
print(max(order))
asd = str(max(order))

for x in range(len(order)):

    if order[0] <= quantity_of_food:
        quantity_of_food -= order.popleft()
    else:
        break

if order:
    result = ""
    for o in range(len(order)):
        result += str(order.popleft()) + " "

    print(f"Orders left: {result}")

else:

    print(f"Orders complete")
