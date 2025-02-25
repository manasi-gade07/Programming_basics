# Calculating the Sum of Digits of a Number Until Single Digit

number = 9875

while number >= 10:
    digit_sum = 0
   
    while number > 0:
        digit_sum += number % 10  
        number = number // 10  
    number = digit_sum  
print(number)
