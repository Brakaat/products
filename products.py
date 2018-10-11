products = []
while True:
    name = input('Type the products name:')
    if name == 'q':
        break
    price = input('Price:')
    products.append([name, price])
print(products)

with open('products.csv', 'w', encoding = 'utf-8') as file:
    file.write('Product,Price\n')
    for p in products:
        file.write(p[0] + ',' + p[1] + '\n')