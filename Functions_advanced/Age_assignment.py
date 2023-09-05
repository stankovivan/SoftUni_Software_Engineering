def get_name(names: tuple, letter: str):
    for name in names:
        if name.startswith(letter):
            return name


def age_assignment(*args, **kwargs):

    people = dict()
    result = ''
    for key, value in kwargs.items():
        name = get_name(args, key)
        people[name] = value

    finished = dict(sorted(people.items(), key=lambda x: x[0]))
    for nam, age in finished.items():
        result += f"{nam} is {age} years old." + "\n"
    return result


print(age_assignment("Peter", "George", G=26, P=19))
