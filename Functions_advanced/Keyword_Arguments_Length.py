def kwargs_length(**kwargs):
    return len(kwargs.keys())


dictionary = {
    "ivan": 25,
    "pesho": 26,
}

print(kwargs_length(**dictionary))
