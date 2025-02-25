# Checking for Armstrong Numbers in a Range

l = int(input('Enter lower limit: '))
u = int(input('Enter upper limit: '))
print(f'Armstrog number in given range are ',end=' ')

for num in range(l, u + 1):  
    arm = 0
    order = len(str(num))  
    temp = num  
    
    while temp > 0:
        rem = temp % 10  
        arm += rem ** order  
        temp //= 10  
    
    if num == arm: 
        print(arm,end=" ")
