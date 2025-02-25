# Generating a Number Pyramid

rows = int(input('Enter rows:'))
for i in range(0, rows+1 ):
    for j in range(1, i + 1):
        print(j, end=" ") 
    print() 
