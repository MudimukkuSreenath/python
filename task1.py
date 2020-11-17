#s1,s2,s3=40,30,70
s1=int(input("enter s1 marks:"))
s2=int(input("enter s2 marks:"))
s3=int(input("enter s3 marks:"))
total=s1+s2+s3
print(total)
perce=total/300*100
print(perce)
if perce>=70:
    print(perce,'is A grade')
elif perce<70 and perce>60 :
    print(perce,'is B grade')
elif perce<60 and perce>50:
    print(perce,'is C grade')
else:
    print(perce,'is D grade')
if s1>s2 and s1>s3:
    print(s1,'is highest')
elif s2>s3:
    print(s2,'is s2 is highest')
else:
    print(s3,'is highest')
if s1<s2 and s1<s3:
    print(s1,'is lowest')
elif s2<s3:
    print(s2,'is  is lowest')
else:
    print(s3,'is lowest')
if s1>35 and s2>35 and s3>35:
    print("pass")
else:
    print("fail")
print(s1)
print(s2)
print(s3)

    
    
