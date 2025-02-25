# Generating a Fibonacci Sequence Using Recursion

def fibonacci(n):
    if n <= 1:
        return n
   
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
number = int(input('Enter number:'))
for i in range(number):
    print(fibonacci(i), end=" ")
