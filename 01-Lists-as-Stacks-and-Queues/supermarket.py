from collections import deque
people = deque()
while True:
    intro = input()
    if intro == "End":
        break

    elif intro == "Paid":
        print("\n".join(people))
        people.clear()
    else:
        people.append(intro)

print(f"{len(people)} people remaining.")