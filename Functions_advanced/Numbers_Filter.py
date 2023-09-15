def even_odd_filter(**kwargs):
    numbers = {}
    for key, val in kwargs.items():
        if key == "even":
            numbers[key] = [x for x in val if x % 2 == 0]
        else:
            numbers[key] = [x for x in val if x % 2 != 0]

    return dict(sorted(numbers.items(), key=lambda x: len(x[1])))


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
    even=[1, 3, 5, 6],
))
