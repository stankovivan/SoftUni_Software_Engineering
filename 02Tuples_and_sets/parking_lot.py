lines = int(input())

car_plates = set()

for x in range(lines):
    intro = input().split(", ")
    command = intro[0]
    car_number = intro[1]
    if command == "IN":
        car_plates.add(car_number)
    elif command == "OUT":
        car_plates.remove(car_number)
if len(car_plates) > 0:
    for plate in car_plates:
        print(plate)
else:
    print(f"Parking Lot is Empty")
