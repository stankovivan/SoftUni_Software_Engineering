lines = int(input())

odd_set = set()
even_set = set()

for x in range(1, lines + 1):
    name = input()
    count = 0

    for character in name:
        count += ord(character)
    count = int(count / x)

    if count % 2 == 0:
        even_set.add(count)

    else:
        odd_set.add(count)

sum_even, sum_odd = sum(even_set), sum(odd_set)
even_set = {str(i) for i in even_set}
odd_set = {str(i) for i in odd_set}

if sum_even == sum_odd:
    result = odd_set.union(even_set)

elif sum_odd > sum_even:
    result = odd_set.difference(even_set)

else:
    result = odd_set.symmetric_difference(even_set)

print(f"{', '.join([str(x) for x in result])}")