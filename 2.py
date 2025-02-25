# Checking for Prime Numbers

num=int(input("Enter number:"))
flag=0
for i in range(2,num):
    if num % i == 0:
        flag += 1
if num > 1 and flag == 0:
    print(f'{num} is prime')
else:
    print(f'{num} is not prime')