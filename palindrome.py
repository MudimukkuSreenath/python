n=;arm=0;temp=n
while n!=0:
    rem=n%10
    arm=arm+(rem**3)
    n=n//10
print(temp,'is reverse is',arm)
if temp==arm:
    print(temp,'is armstong')
else:
    print(temp,'is not armstrong')
