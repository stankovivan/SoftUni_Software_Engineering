rows, clons = [int(e) for e in input().split(", ")]
matrix = []
big_sum = []
biggest_sum = 0

for _ in range(rows):
    nums = [int(num) for num in input().split(", ")]
    matrix.append(nums)

for i in range(rows - 1):
    for j in range(clons - 1):
        sum_int = 0
        m = []
        for x in range(i, i + 2):
            la = []
            for z in range(j, j + 2):
                sum_int += matrix[x][z]
                la.append(matrix[x][z])
            m.append(la)

        if sum_int > biggest_sum:
          biggest_sum = sum_int
          big_sum = m

for element in big_sum:
    print(*element)
print(biggest_sum)
