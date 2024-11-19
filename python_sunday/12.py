brands = ['nike','puma','adidas']

info = input('Enter Brand Name:')

if info == "":
    print('Please enter a brand name')
elif info in brands:
        print('Name Already Exists')
else:
    brands.append(info)
    print(brands) 

del brands[0]
print(brands)

brands.clear()