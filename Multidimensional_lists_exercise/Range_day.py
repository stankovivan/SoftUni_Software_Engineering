def move(direction, step):
    r = my_pos[0] + directions[direction][0] * step
    c = my_pos[1] + directions[direction][1] * step
    if not (0 <= r < size and 0 <= c < size):
        return my_pos
    if pole[r][c] == "x":
        return my_pos
    return [r, c]


def shoot(direction):
    r = my_pos[0] + directions[direction][0]
    c = my_pos[1] + directions[direction][1]

    while 0 <= r < size and 0 <= c < size:
        if pole[r][c] == 'x':
            pole[r][c] = "."
            return [r, c]
        r += directions[direction][0]
        c += directions[direction][1]


size = 5
pole = []
target = 0
target_hits = 0
target_hits_pos = []
my_pos = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
for row in range(size):
    line = input().split(" ")
    pole.append(line)
    if "A" in line:
        my_pos = [row, line.index("A")]
        pole[row][my_pos[1]] = "."
    target += line.count("x")

for x in range(int(input())):
    command_info = input().split()

    if command_info[0] == "move":
        my_pos = move(command_info[1], int(command_info[2]))
    elif command_info[0] == "shoot":
        target_d_pos = shoot(command_info[1])

        if target_d_pos:
            target_hits_pos.append(target_d_pos)
            target_hits += 1

        if target_hits == target:
            print(f"Training completed! All {target} targets hit.")
            break
if target_hits < target:
    print(f"Training not completed! {target - target_hits} targets left.")
[print(target_pos) for target_pos in target_hits_pos]
