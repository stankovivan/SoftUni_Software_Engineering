row = int(input())
matrix = [input().split(" ") for x in range(row)]
diagonal = []
diagonal_back = []

for index in range(row):
    diagonal.append(matrix[index][index])
    diagonal_back.append(matrix[index][row - index - 1])

sum_diagonal = sum(int(x) for x in diagonal)
sum_diagonal_back = sum(int(x) for x in diagonal_back)
diff = abs(sum_diagonal - sum_diagonal_back)
print(diff)
