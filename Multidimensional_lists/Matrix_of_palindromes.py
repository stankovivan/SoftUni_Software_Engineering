rows, cols = tuple(map(int, input().split(" ")))
first_letter = 97

for row in range(rows):
    matrix = []
    for col in range(cols):
        ascii_table = chr(first_letter + row) + chr(first_letter + col + row) + chr(first_letter + row)
        matrix.append(ascii_table)
    print(*matrix)

