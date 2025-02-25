# Finding the Fibonacci Number at a Specific Position

num = int(input('Enter position: ')) 
l = []
a = 0
b = 1

for i in range(0, num+1 ): 
    l.append(a)
    c = a + b
    a = b
    b = c

print(f'The Fibonacci number at position {num} is {l[-1]}')
