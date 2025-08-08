def car_exp():
    yield "Porche"
    yield "Ferrari"

def car_bud():
    yield "Tata"
    yield "Hyundai"
    yield "Suzuki"

def car_package():
    yield from car_exp()
    yield from car_bud()

for cars in car_package():
    print(cars)

def car_shop():
    try:
        while True:
            order = yield "Waiting for next car order"
    except:
        print("Shop closed, No more Cars to buy!")

shop = car_shop()
print(next(shop))
shop.close() # cleanup
