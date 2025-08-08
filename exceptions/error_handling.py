chai_menu = {
    "masala chai" : 30,
    "ginger chai" : 40
}

try:
    chai_menu["lemon tea"]
except KeyError:
    print("The key that you are typing to access does not exists.")

print("Hello Rabi!")