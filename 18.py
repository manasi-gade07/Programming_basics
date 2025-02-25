# Generating Multiplication Tables

n = int(input('Enter number:'))
for i in range(1,11):
    res = n * i
    print(f'{n} x {i} = {res}')