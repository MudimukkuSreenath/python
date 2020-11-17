import copy
l1=[10,20,[30,40],50]
l2=copy.deepcopy(l1)
l1[0]=111
l1[2][0]=100
print(l1)
print(l2)
