class Coffee:
    origin = "India"
    
print(Coffee.origin)

Coffee.is_hot = True 
print(Coffee.is_hot)

# Creating objects from class Coffee

latte = Coffee()
print(f"Latte {latte.origin}")
print(f"Latte {latte.is_hot}")

latte.is_hot = False

print(f"Class : ", Coffee.is_hot)
print(f"Latte {latte.is_hot}")

latte.flavour = "milky"
print(latte.flavour)
