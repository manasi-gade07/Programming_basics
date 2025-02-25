# Finding the Sum of the Digits of the Factorial of a Number

n = int(input('Enter number:'))
flag = 1
for i in range(1,n+1):
    flag *= i
tmp = flag
sum = 0
while flag > 0:
    rem = flag % 10
    sum += rem
    flag = flag // 10
print(f'The factorial of {n} is {tmp}, and the sum of the digits is {sum}')