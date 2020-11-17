num = int(input('How many numbers: '))
sum = 0
for n in range(num):
    
    numbers = int(input('Enter number : '))
    sum += numbers
    avg =sum/num
print('sum of digits',sum)
print('Average of ', num, ' numbers is :', avg)
