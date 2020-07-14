import json

with open('product.json') as jfile:
    datos = json.load(jfile)
    print(datos['name'])
    print(datos['price'])
    print(datos['weight'])
