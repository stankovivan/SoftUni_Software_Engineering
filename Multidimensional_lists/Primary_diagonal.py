cols = int(input())
matrix = []

for _ in range(cols):
    matrix.append([int(x) for x in input().split(" ")])
dig = 0

for index in range(cols):
    dig += matrix[index][index]

print(dig)
