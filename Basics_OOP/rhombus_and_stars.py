n = int(input())
for row in range(1, n + 1):
    print(" " * (n - row), end="")
    for col in range(1, row + 1):
        print("* ", end="")
    print()
for row in range(n - 1, -1, -1):
    print(" " * (n - row), end="")
    for col in range(1, row + 1):
        print("* ", end="")
    print()
