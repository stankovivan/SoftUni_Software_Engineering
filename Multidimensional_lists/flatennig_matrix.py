intro = int(input())
matrix = []

for _ in range(intro):
    row = [int(x) for x in input().split(", ")]
    matrix.extend(row)
print(matrix)
