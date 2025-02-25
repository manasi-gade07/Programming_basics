# Finding the Number of Digits in a Number

n = int(input('Enter number:'))
tmp = n
digit = 0
while n > 0:
    rem = n % 10
    digit += 1
    n = n//10
print(f'The number {tmp} has {digit} digits')