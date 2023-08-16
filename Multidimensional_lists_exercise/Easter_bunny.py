seize = int(input())
matrix = []
bunny_pos = []
best_path = []
best_direction = None
max_collected_eggs = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
for row in range(seize):
    line = input().split()
    if "B" in line:
        bunny_pos = [row, line.index("B")]
    matrix.append(line)
for direction, possitions in directions.items():
    row, col = [
        bunny_pos[0] + possitions[0],
        bunny_pos[1] + possitions[1]
    ]
    path = []
    collected_eggs = 0
    while 0 <= row < seize and 0 <= col < seize:
        if matrix[row][col] == "X":
            break

        collected_eggs += int(matrix[row][col])
        path.append([row, col])
        row += possitions[0]
        col += possitions[1]
    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_direction = direction
        best_path = path
print(best_direction)
print(*best_path, sep="\n")
print(max_collected_eggs)
