intro = int(input())

matrix = []

for _ in range(intro):
    bow = [int(num) for num in input().split(", ") if int(num) % 2 == 0]
    matrix.append(bow)
print(matrix)
