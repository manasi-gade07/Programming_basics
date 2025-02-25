# Finding the Sum of Squares of Digits  

n = int(input('Enter number:'))
tmp = n
digi_sum = 0
while n > 0:
    rem = n % 10
    digi_sum += rem ** 2
    n = n // 10
print(f'The sum of the squares of digits in number {tmp} is {digi_sum}')