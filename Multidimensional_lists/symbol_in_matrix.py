intro = int(input())
matrix = []
condition = True

for z in range(intro):
    matrix.append(list(input()))
wanted = input()
condition = False

for row in range(intro):
    for col in range(intro):
        if matrix[row][col] == wanted:
            print(f"({row}, {col})")
            condition = True
            break
    if condition:
        break
if not condition:
    print(f"{wanted} does not occur in the matrix")
