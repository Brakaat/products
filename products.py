# read file
import os #operating system > find the file authority
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as file:
            for line in file:
                if 'Product,Price' in line:
                    continue
                name, price = line.strip().split(',')
                products.append([name, price])
    print(products)
    return products

# user input
def user_input(products):
    while True:
        name = input('Type the products name:')
        if name == 'q':
            break
        price = input('Price:')
        products.append([name, price])
    print(products)
    return products

# write .csv
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as file:
        file.write('Product,Price\n')
        for p in products:
            file.write(p[0] + ',' + p[1] + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): #相對路徑> same folder
        print('The file is exist')
        products = read_file(filename)
    else:
        print('The file is not exsit')
    products = user_input(products)
    write_file(filename, products)

main()
