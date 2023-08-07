cols, rows = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(cols):
    matrix.append([int(x) for x in input().split(" ")])

for row in range(rows):
    total = 0

    for col in range(cols):
        total += matrix[col][row]
    print(total)
