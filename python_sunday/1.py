"""
def homeloancalculator():
"""

def homeloancalculator(P,R,N):
    N = N*12
    R = R/12/100
    emi = P*R*(1+R)**N/((1+R)**N-1)
    print("EMI:" , emi)

homeloancalculator(100000,8,30)
homeloancalculator(200000,8,30)        

