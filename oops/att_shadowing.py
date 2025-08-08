class Coffee:
    temperature = "Hot"
    strength = "Strong"
    
cupped = Coffee()
print(cupped.temperature)

cupped.temperature = "Mild"
cupped.cup_size = "small"

print("After changing : ", cupped.temperature)
print("Direct look into the class : ", Coffee.temperature)
print("Cup size is : ", cupped.cup_size)

del cupped.temperature
del cupped.cup_size
print(cupped.temperature)
print(cupped.cup_size)