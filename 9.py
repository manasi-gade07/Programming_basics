# Summing Digits of a Number

n =int(input('enter number:'))
sum = 0
while n > 0:
    rem = n % 10
    sum += rem
    n = n // 10
print(f'Sum of digits in number is {sum}')
