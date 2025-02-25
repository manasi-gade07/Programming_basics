# Finding the Largest and Smallest Numbers in an Array

a = [4, 7, 1, 8, 5]
largest = a[0]
smallest = a[0]

for i in range(1,len(a)):
    if a[i] > largest:
        largest = a[i]
    if a[i] < smallest:
        smallest = a[i]
print('Largest :',largest,'smallest :',smallest)

