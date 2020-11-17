def emi_calculator(p, r, t): 
    r = r / (12 * 100) # one month interest 
    t = t * 12 # one month period 
    emi = (p * r * pow(1 + r, t)) / (pow(1 + r, t) - 1) 
    return emi 
  
# driver code 
principal = 500000; 
rate = 1.5; 
time = 1; 
emi = emi_calculator(principal, rate, time); 
print("Monthly EMI is= ", emi) 
