rows = int(input())
matrix = []

for colons in range(rows):
    matrix.append(list(map(int, input().split(" "))))
#print(matrix)


command = input().split(" ")
while command[0] != "END":
    row, col, values = int(command[1]), int(command[2]), int(command[3])
    if row < 0 or row >= rows or col < 0 or col >= rows:
        print(f"Invalid coordinates")

    elif command[0] == "Add":
        matrix[row][col] += values
    elif command[0] == "Subtract":
        matrix[row][col] -= values
    command = input().split(" ")

[print(*row) for row in matrix]
