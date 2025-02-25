# Generating a Square Matrix of a Given Size

size = int(input('Enter size:'))
matrix = []
num = 1
for i in range(size):
    row = []  
    for j in range(size):
        row.append(num)  
        num += 1 
    matrix.append(row)  
for row in matrix:
    print(" ".join(map(str, row)))
