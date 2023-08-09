from sys import maxsize

rows, colons = map(int, input().split(" "))
matrix = [input().split(" ") for x in range(rows)]
square_sum_big = []
big_sq_sum = -maxsize

for row in range(rows - 2):
    for col in range(colons - 2):
        square = [
                list(map(int, [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]])),
                list(map(int, [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]])),
                list(map(int, [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]))
        ]

        square_sum = sum(sum(square, []))
        if square_sum > big_sq_sum:
            big_sq_sum = square_sum
            square_sum_big = square

print(f"Sum = {big_sq_sum}")
for wit in square_sum_big:
    print(' '.join(list(map(str, wit))))
