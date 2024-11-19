products = [
    {
        "name":"Jeans",
        "price":1000,
        "discount":20,
        "size":["XL","L"]
    },
    {
        "name":"kurta",
        "price":1000,
        "discount":20,
        "size":["XL","L"]
    },
    {
        "name":"belt",
        "price":1000,
        "discount":20,
        "size":["XL","L"]
    }
]

for val in products:
    # print(val)
    for k,v in val.items():
        print(v,end=" ")
    print("\n")