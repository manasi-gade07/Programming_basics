# Printing Prime Numbers Less Than a Given Number

n = int(input('Enter number:'))

for num in range(2,n):
    flag = 0
    for i in range(2,num):
        if num % i == 0:
            flag += 1
            break
    if flag == 0:
        print(num,end=' ')
 

