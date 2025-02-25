# Calculating Armstrong Numbers

num = int(input('Enter number:'))
arm = 0
tmp = num
ord= len(str(num))
while tmp > 0:
    rem = tmp % 10
    arm = (rem ** ord) + arm
    tmp = tmp // 10
if num == arm:
    print(f'{arm} is armstrong number')
else:
    print(f'{arm} is not armstrong number')