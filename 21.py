#Calculating the Sum of Even Numbers in a Range

a = int(input('Enter lower limit:'))
b = int(input('Enter upper limit:'))
sum = 0
for i in range(a,b+1):
    if i % 2 == 0:
        sum += i
print(f'The sum of even numbers in range is {sum}')