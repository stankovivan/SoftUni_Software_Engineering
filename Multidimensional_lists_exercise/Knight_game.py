board_size = int(input())

matrix = [list(input()) for x in range(board_size)]
position = (
    (-2, 1),
    (-2, -1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2),
)
removed = 0
while True:
    max_attack = 0
    position_for_most_attack = []
    for row in range(board_size):
        for col in range(board_size):

            if matrix[row][col] == "K":
                atack = 0

                for pos in position:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]
                    if 0 <= pos_row < board_size and 0 <= pos_col < board_size:

                        if matrix[pos_row][pos_col] == "K":
                            atack += 1
                if atack > max_attack:
                    position_for_most_attack = [row, col]
                    max_attack = atack
    if position_for_most_attack:
        matrix[position_for_most_attack[0]][position_for_most_attack[1]] = "0"
        removed += 1
    else:
        break

print(removed)
