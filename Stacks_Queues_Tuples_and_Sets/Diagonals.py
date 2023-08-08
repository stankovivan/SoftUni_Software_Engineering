rows = int(input())
matrix = [input().split(", ") for i in range(rows)]
sum_diagonals = []
second = []
for index in range(rows):
    sum_diagonals.append(matrix[index][index])
    second.append(matrix[index][rows - index - 1])

print(f"Primary diagonal: {', '.join(sum_diagonals)}. Sum: {sum(int(x) for x in sum_diagonals)}")
print(f"Secondary diagonal: {', '.join(second)}. Sum: {sum(int(x) for x in second)}")
