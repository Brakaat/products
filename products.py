products = []
while True:
    name = input('Type the products name:')
    if name == 'q':
        break
    price = input('Price:')
    p = []
    p.append(name)
    p.append(price)
    products.append(p)
print(products)

