# Calculating the Sum of Odd Numbers in a Range

a = int(input('Enter lower limit:'))
b = int(input('Enter upper limit:'))
sum = 0
for i in range(a,b+1):
    if i % 2 != 0:
        sum += i
print(f'The sum of odd numbers in range is {sum}')