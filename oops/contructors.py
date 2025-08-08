class ChaiOrder:
    def __init__(self,type_, size):
        self.type = type_
        self.size = size
        
    def summary(self):
        return f"{self.size}ml of {self.type} chai"


order_1 = ChaiOrder("Masala", 200)
print(order_1.summary())

order_2 = ChaiOrder("Lemon Iced", 400)
print(order_2.summary())