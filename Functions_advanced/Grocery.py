def grocery_store(**kwargs):
    dictionary_sorted = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = ''
    for key, val in dictionary_sorted:
        result += f"{key}: {val}" + "\n"
    return result


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
