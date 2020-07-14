import json
from product import *

def create_product():
    name = str(input("Product's name:\n"))
    price = int(input("Product's price\n"))
    weight = int(input("Product's weight\n"))
    product = Product(1, name, price, weight)
    return product


if __name__ == '__main__':
    product = create_product()
    with open('product.json', 'w') as jfile:
        json.dump(product.__dict__, jfile, indent = 4)




    
