laptop_prices_inr = {
    "HP" : 45000,
    "ASUS" : 50000,
    "ACER" : 30000,
    "LENOVO" : 50000,
    "APPLE" : 90000
}

laptop_prices_usd = {laptop:price / 80 for laptop, price in laptop_prices_inr.items()}
print(laptop_prices_usd)