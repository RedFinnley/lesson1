stock = [
    {'name': "Айфон", "stock": 24, 'price': 65000, 'recomend': ['Samsung', 'Xiaomi']},
    {'name': 'Xiaomi', 'stock': 85, 'price': 55000, 'discount': 5000},
    {'name': 'Samsung', 'stock': 55, 'price': 54000},
]
print(type(stock))
print(type(stock[0]))
print(stock[0]['recomend'][0])