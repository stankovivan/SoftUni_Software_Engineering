def recursive_power(number, power):
    return number ** power

def da(number):
    if number == 1:
        return 1
    else:
        return number * da(number - 1)




print(da(3))

#print(recursive_power(10, 100))
