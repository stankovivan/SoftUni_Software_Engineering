intro = [int(x) for x in input().split(" ")]


def negative_vs_positive(command: str, numbers_list: list):
    if command == "negative":
        ne_list = [int(x) for x in numbers_list if x < 0]
    else:
        ne_list = [int(x) for x in numbers_list if x > 0]
    rev_list = sum(ne_list)
    print(sum(ne_list))
    return rev_list


sum_neg = negative_vs_positive("negative", intro)
sum_pos = negative_vs_positive("positive", intro)
if abs(sum_neg) < abs(sum_pos):
    print(f"The positives are stronger than the negatives")
else:
    print(f"The negatives are stronger than the positives")


# quick_test = 1 2 -3 -4 65 -98 12 57 -84
