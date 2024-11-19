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
    


ppfCalculator(150000,7.1,15)