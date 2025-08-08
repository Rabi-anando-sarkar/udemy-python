# normal function

def get_car_list():
    return ["Car 1", "Car 2", "Car 3"]

# generator 

def get_car_gen():
    yield "Car 1"
    yield "Car 2"
    yield "Car 3"
    

car1 = get_car_list()
print(car1)

car2 = get_car_gen()
print(next(car2))
print(next(car2))
print(next(car2))
# print(next(car2))