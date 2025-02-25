# Finding the Median of an Array

rows = int(input('Enter rows:'))
triangle = []

for i in range(rows):
    row = [1] * (i + 1)  
    for j in range(1, i):
        row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)

for row in triangle:
    print(" ".join(map(str, row)))
