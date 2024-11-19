days = {'monday','tuesday','wednesday','thursday','friday','saturday','sunday','sunday','wednesday'}

print(days)
print(type(days))
print(len(days))

for val in days:
    print(val)

days.add('jan')
days.remove('monday')

print(days)