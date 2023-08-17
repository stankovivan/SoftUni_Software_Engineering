def cookie(coun_presents_left, nice_kids):
    for cordinates in directions.values():
        r = santa_po[0] + cordinates[0]
        c = santa_po[1] + cordinates[1]
        if kvartal[r][c].isalpha():
            if kvartal[r][c] == "V":
                nice_kids += 1

            kvartal[r][c] = "-"
            coun_presents_left -= 1
        if not coun_presents_left:
            break
    return coun_presents_left, nice_kids


coun_presents = int(input())
size_neighood = int(input())

kvartal = []
santa_po = []
total_nice_kids = 0
nice_kids_vis = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
for row in range(size_neighood):
    line = input().split(" ")
    kvartal.append(line)
    if "S" in line:
        santa_po = [row, line.index("S")]
        kvartal[row][santa_po[1]] = "-"
    total_nice_kids += line.count("V")
command = input()

while True:
    if command == "Christmas morning":
        break

    santa_po = [
        santa_po[0] + directions[command][0],
        santa_po[1] + directions[command][1]
    ]
    house = kvartal[santa_po[0]][santa_po[1]]
    if house == "V":
        nice_kids_vis += 1
        coun_presents -= 1
    elif house == "C":
        coun_presents, nice_kids_vis = cookie(coun_presents, nice_kids_vis)
    kvartal[santa_po[0]][santa_po[1]] = "-"
    if not coun_presents or nice_kids_vis == total_nice_kids:
        break
    command = input()
kvartal[santa_po[0]][santa_po[1]] = "S"
if not coun_presents and nice_kids_vis < total_nice_kids:
    print(f"Santa ran out of presents!")
print(*[' '.join(row) for row in kvartal], sep="\n")
if nice_kids_vis == total_nice_kids:
    print(f"Good job, Santa! {nice_kids_vis} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_vis} nice kid/s.")
