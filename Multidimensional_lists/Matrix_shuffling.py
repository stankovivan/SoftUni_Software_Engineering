rows, colons = tuple(map(int, input().split(" ")))
matrix = [input().split(" ") for i in range(rows)]

while True:
    command = input()
    if command == "END":
        break
    command = command.split(" ")

    if 'swap' not in command or len(command) != 5:
        print(f"Invalid input!")
        continue
    com = list(map(int, command[1:]))
    if False in [
            0 <= com[0] < rows,
            0 <= com[1] < colons,
            0 <= com[2] < rows,
            0 <= com[3] < colons]:
        print(f"Invalid input!")
        continue

    p1, p2 = matrix[com[0]][com[1]], matrix[com[2]][com[3]]
    matrix[com[0]][com[1]] = p2
    matrix[com[2]][com[3]] = p1

    for r in matrix:
        print(*r)

