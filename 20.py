# Checking for Perfect Numbers

n = int(input('Enter number:'))
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum += i
if n == sum:
    print(f'{n} is perfect number')
else:
    print(f'{n} is not perfect number')