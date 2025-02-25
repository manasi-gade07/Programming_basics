# Finding the Count of Specific Digits in a Number

n = int(input('Enter number: '))
digit = int(input('Enter digit to count: '))

tmp = n 
count = 0

while n > 0:
    rem = n % 10  
    if rem == digit:  
        count += 1
    n = n // 10  
print(f'The digit {digit} occurs {count} times in the number {tmp}')

