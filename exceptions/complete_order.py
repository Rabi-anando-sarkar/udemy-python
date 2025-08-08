class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 20,"ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("that chai is available")
        if not isinstance(cups, int):
            raise TypeError("Number os cups must be an int value")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai: rupees {total}")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank you for visiting us!")

bill("mint",10)
bill("masala",5)
bill("ginger","four")