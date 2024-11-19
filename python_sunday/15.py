product = {
    "name":"Jeans",
    "price":1000,
    "discount":20,
    "size":["XL","L"]
}

print(product)
print(type(product))
print(len(product))

for key in product:
    print(key , product[key])

for ans in product.values():
    print(ans)

for ans in product.keys():
    print(ans)

for k,v in product.items():
    print(k,v)

product['name'] = 'Blue Jeans'
print(product)