clothes = list(map(int, input().split(" ")))
capacity = int(input())
racks = 1
temp = 0

for _ in range(len(clothes)):
    if temp + clothes[-1] > capacity:
        racks += 1
        temp = clothes.pop()
    elif temp + clothes[-1] == capacity:
        temp = 0
        clothes.pop()
        if clothes:
            racks += 1
    else:
        temp += int(clothes.pop())
print(racks)
