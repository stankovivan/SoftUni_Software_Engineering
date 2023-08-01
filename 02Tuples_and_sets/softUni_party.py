lines = int(input())
guest_list = set()
arrived_guest = set()
for x in range(lines):
    guest_list.add(input())

arrival = input()
while arrival != "END":
    arrived_guest.add(arrival)
    arrival = input()

missing = guest_list.difference(arrived_guest)
print(len(missing))
for guest in sorted(missing):
    print(guest)
