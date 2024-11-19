brands = ['nike','puma','adidas','puma','puma']
print(brands)
print(len(brands))
print(type(brands))

print(brands[0])
print(brands[1])

print(brands[-1])

print("----- using for in loops-----")

brands.append('zara')
brands.insert(2,'tata')

brands.pop()
brands.remove('nike')
print(brands)

for val in brands:
    print(val)