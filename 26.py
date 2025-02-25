# Checking if a Number is a Narcissistic Number

n = int(input('Enter number:'))
ord = len(str(n))
sum = 0
tmp = n
while n > 0:
    rem = n % 10
    sum += rem ** ord
    n = n // 10
if tmp == sum:
    print(f'{tmp} is Narcissistic Number')
else:
        print(f'{tmp} is  not Narcissistic Number')

    