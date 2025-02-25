# Finding the Greatest Common Divisor (GCD)

a = int(input('Enter lower limit:'))
b = int(input('Enter upper limit:'))
gcd = 1
for i in range(1,min(a,b)):
    if a % i == 0 and b % i == 0:
        gcd = i
print(f'The GCD of {a} and {b} is {gcd}')

