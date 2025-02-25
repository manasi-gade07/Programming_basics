# Finding the Least Common Multiple (LCM)

a = int(input('Enter lower limit:'))
b = int(input('Enter upper limit:'))
gcd = 1
lcm = 1
for i in range(1,min(a,b)):
    if a % i == 0 and b % i == 0:
        gcd = i
lcm = (a * b)//gcd
print(f'The LCM of {a} and {b} is {lcm}')
