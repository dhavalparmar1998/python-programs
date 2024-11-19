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
    print("EMI" , emi)


if(P=="" or R=="" or N==""):
    print("All Values Required")
else:
    P = int(P)
    R = float(R)
    N = int(N)
    homeloancalculator(P,R,N)        