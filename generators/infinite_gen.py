def infinite_car():
    count = 1
    while True:
        yield f"Car bought #{count}"
        count += 1
        
car_buyer_1 = infinite_car()

for _ in range(5):
    print(next(car_buyer_1))

car_buyer_2 = infinite_car()

for _ in range(3):
    print(next(car_buyer_2))