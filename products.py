# read .csv
products = []
with open('products.csv', 'r', encoding = 'utf-8') as file:
    for line in file:
        if 'Product,Price' in line:
            continue
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)

# user input
while True:
    name = input('Type the products name:')
    if name == 'q':
        break
    price = input('Price:')
    products.append([name, price])
print(products)

# write .csv
with open('products.csv', 'w', encoding = 'utf-8') as file:
    file.write('Product,Price\n')
    for p in products:
        file.write(p[0] + ',' + p[1] + '\n')