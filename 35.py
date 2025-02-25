# Finding the Sum of Prime Numbers in a Range
a = int(input('Enter lower limit:'))
b = int(input('Enter upper limit:'))

sum = 0
for num in range(a,b):
    flag = 0
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                flag += 1
        if flag == 0:
            sum += num
print(f'The sum of prime numbers between {a} and {b} is {sum}')
