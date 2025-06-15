mobiles = [
    {"name": "Apple", "model": "iphone 16 Pro Max", "ram": 8, "camera": "48MP + 48MP + 12MP", "price": 135900},
    {"name": "Samsung", "model": "Galaxy 2 Fold6", "ram": 12, "camera": "50MP + 12MP + 10MP", "price": 138990},
    {"name": "Google", "model": "Pixel 9 Pro XL", "ram": 12, "camera": "50MP + 48MP + 48MP", "price": 124999},
    {"name": "Vivo", "model": "X Fold3 Pro", "ram": 12, "camera": "50MP + 64MP + 58MP", "price": 87590},
    {"name": "Samsung", "model": "Galaxy S25 Ultra", "ram": 12, "camera": "200MP + 50MP + 10MP + 50MP", "price": 117999},
    {"name": "Xiaomi", "model": "15 ultra", "ram": 12, "camera": "50MP + 58MP + 200MP", "price": 109998},
    {"name": "OnePlus", "model": "18 Pro 5G", "ram": 8, "camera": "48MP + 50MP + 8MP", "price": 50199},
    {"name": "Sony", "model": "Xperia 1 IV", "ram": 12, "camera": "12MP + 12MP + 12MP", "price": 108999},
    {"name": "Apple", "model": "iphone 16 Plus", "ram": 8, "camera": "Dual Primary Camera", "price": 126999},
    {"name": "Vivo", "model": "X200 Pro", "ram": 12, "camera": "50MP + 50MP + 200MP", "price": 87590}
]

for mble in mobiles:
    if mble["ram"] > 8 and mble["price"] < 120000:
        print(mble)