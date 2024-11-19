days = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','sunday','wednesday')

print(days)
print(type(days))
print(len(days))

print(days[0])
print(days[-1])

days = ('monday','tuesday')
print(days)
for val in days:
    print(val)


del days
print(days)