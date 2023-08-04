lines = int(input())
longest_inter = {}

for _ in range(lines):
    left_range, right_range = input().split("-")
    left_range_start, left_range_end = tuple(map(int, left_range.split(",")))
    right_range_start, right_range_end = tuple(map(int, right_range.split(",")))
    left_set = {num for num in range(left_range_start, left_range_end + 1)}
    right_set = {num for num in range(right_range_start, right_range_end + 1)}
    intersection = left_set & right_set

    if len(intersection) > len(longest_inter):
        longest_inter = intersection

print(f'Longest intersection is [{", ".join(map(str, {i for i in longest_inter}))}] with length {len(longest_inter)}')
