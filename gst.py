f1=float(input("enter biriyani amount:"))
f2=float(input("enter rice amount:"))
f3=float(input("enter chiken amount:"))
f4=float(input("enter dosa amount:"))
f5=float(input("enter panipuri amount:"))
total=f1+f2+f3+f4+f5
print("total:",total)
per=total*0.05
cgst=total+per
print("cgst",per)
per1=cgst*0.05
sgst=cgst+per1
print("sgst=",per1)
dis=sgst*0.10
print("discount:",dis)
print("Total amount=",sgst-dis)
         
