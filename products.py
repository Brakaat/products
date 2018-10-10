products = []
while True:
    name = input('Type the products name:')
    if name == 'q':
        break
    price = input('Price:')
    products.append([name, price])
print(products)

