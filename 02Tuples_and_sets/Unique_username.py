lines = int(input())
usernames = []

for n in range(lines):
    name = input()

    if name not in usernames:
        usernames.append(name)
        print(name)
