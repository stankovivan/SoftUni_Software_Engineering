def fill_the_box(*args):

    capacity = 1
    to_fill = 0

    for index, number in enumerate(args):
        if number == "Finish":
            break
        if index < 3:
            capacity *= number
        else:
            to_fill += number
    if capacity > to_fill:
        return f"There is free space in the box. You could put {capacity - to_fill} more cubes."
    else:
        return f"No more free space! You have {abs(to_fill - capacity)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
