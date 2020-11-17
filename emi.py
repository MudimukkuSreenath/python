p=float(input("enter amount:"))
r=float(input("enter the rate:"))
n=int(input("enter tenure(months):"))
E=((p*r)*((1+r)**n))/((1+r)**n-1)
print("u have to pay this amount:",E)
      
