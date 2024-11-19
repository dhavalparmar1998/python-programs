def ppfCalculator(amount,roi,duration):
    # print('Function calculator')
    year=1
    openingBalance=0
    while year<=duration:
        interest = (openingBalance+amount)*roi/100
        interest = round(interest)
        closingBalance = openingBalance+amount+interest
        print('Year',year,'OB',openingBalance,'interest',interest,'CB',closingBalance)
        year+=1
        openingBalance = closingBalance

def simpleInterestCalculator(p,r,t):
    si = p*r*t/100
    finalBalance = si + p
    print(si , finalBalance)

def productDiscount(amount,discount):
    discountValue = amount*discount/100
    finalPrice = amount - discountValue
    return [discountValue,finalPrice] 


def productDiscount_t(amount,discount):
    discountValue = amount*discount/100
    finalPrice = amount - discountValue
    return (discountValue,finalPrice)


def productDiscount_d(amount,discount):
    discountValue = amount*discount/100
    finalPrice = amount - discountValue
    return {
        "discountByUser": discountValue,
        "finalAmount":finalPrice
    }