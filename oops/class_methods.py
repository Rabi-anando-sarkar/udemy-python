class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )
        
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(
            tea_type,
            sweetness,
            size
        )

class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]
    
print(ChaiUtils.is_valid_size("Medium"))

order_1 = ChaiOrder.from_dict({"tea_type" : "masala chai", "sweetness" : "no", "size" : "large"})

order_2 = ChaiOrder.from_string("Ginger-low-small")

order_3 = ChaiOrder("lemon tea", "yes", "medium")

print(order_1.__dict__)
print(order_2.__dict__)
print(order_3.__dict__)
