# Finding the N-th Triangular Number

N = int(input('Enter triangular number:'))
triangular_number = 0
for i in range(1, N + 1):
    triangular_number += i
print(triangular_number)
