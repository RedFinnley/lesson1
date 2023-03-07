
discounted(100, 50, max_discount=100)
product = {'Name': 'Samsung', 'stock': 20, 'price': 50000, 'discount': 70}
product['with_discount'] = discounted(product['price'], product['discount'], max_discount = 80)
print(product) 