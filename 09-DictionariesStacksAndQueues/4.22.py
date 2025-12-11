import json

product = {}

name = input('Podaj nazwę produktu: ')
price = input('Podaj cenę produktu: ')
paid = input('Czy zapłacono?[Yes/No]') == 'Yes'

priceD = float(price)
priceD = format(priceD,'.2f')

product['name'] = name
product['price'] = priceD
product['paid'] = paid

file_name = 'product.json'
with open(file_name, 'w') as file:
    json.dump(product, file)

print('Data has been written to', file_name)