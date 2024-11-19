P = input("Enter Loan Amount:")
# print(P, type(P))
R = input("Enter ROI:")
# print(R, type(R))
N = input("Enter Duration:")
# print(N, type(N))




def homeloancalculator(P,R,N):
    N = N*12
    R = R/12/100
    emi = P*R*(1+R)**N/((1+R)**N-1)
    # print("EMI" , emi)
    # return emi
    payableamount = emi*N
    interestamount = payableamount - P
    return[emi, payableamount, interestamount]


if(P=="" or R=="" or N==""):
    print("All Values Required")
else:
    P = int(P)  # type casting
    R = float(R)
    N = int(N)
    # homeloancalculator(P,R,N)    
    result = homeloancalculator(P,R,N)
    print("EMI: ",result[0])    
    print("Total Payableamount: ",result[1])    
    print("Total Interestamount: ",result[2])    
    print("Loan Amount: ",P)    

    