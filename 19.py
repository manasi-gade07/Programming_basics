# Finding Prime Numbers in a Range

a = int(input('Enter lower limit:'))
b = int(input('Enter upper limit:'))
print(f' Prime numbers between {a} and {b} are',end=' ')

for num in range(a,b+1):
    flag = 0
    for i in range(2,num):
        if num % i == 0:
            flag += 1
            break
    if flag == 0 and num > 1:
        print(num,end=' ')
