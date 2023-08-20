def sorting_cheeses(**kwargs):
    result_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result_key = ''
    for key, value in result_cheese:
        sorted_values = sorted(value, reverse=True)
        result_key += key + "\n"
        result_key += "\n".join(str(x) for x in sorted_values) + "\n"
    return result_key


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
