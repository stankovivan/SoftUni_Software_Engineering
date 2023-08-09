rows, cols = tuple(map(int, input().split(" ")))
snake = input()
matrix = []
counter = 0

for row in range(rows):
    res = ""
    for col in range(cols):
        res += snake[counter % len(snake)]
        counter += 1

    if row % 2 == 0:
        matrix.append(res)
    else:
        matrix.append(res[::-1])

    res = ""
    for col in range(cols):
        res += matrix[row][col]

for sub in matrix:
    print(*sub, sep="")
