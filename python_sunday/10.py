from custommodule import * 

print("calling custom module")

ppfCalculator(150000 , 7.1, 15)
simpleInterestCalculator(10000,9,30)

ans = productDiscount(10000,30)
print(ans , type(ans))
print(ans[0])
print(ans[1])

ans[0]=9999
print(ans , type(ans))


ans = productDiscount_t(10000,30)
print(ans , type(ans))
print(ans[0])
print(ans[1])
# ans[0]=9999

ans = productDiscount_d(10000,30)
print(ans , type(ans))
print(ans['discountByUser'] )
print(ans['finalAmount'] )