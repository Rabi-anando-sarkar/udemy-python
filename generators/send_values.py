def car_customer():
    print("What car wpuld you like ?")
    order = yield # this only runs when we start the generator
    while True:
        print(f"Building: {order}")
        order = yield
        
stall = car_customer()
next(stall) # start the generator

stall.send("Porche")
stall.send("Ferrai")