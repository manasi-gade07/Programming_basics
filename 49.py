# Finding the Second Largest Number in an Array

a=[10, 20, 4, 45, 99]

largest = a[0]
slargest= -1
for i in range(len(a)):
    if a[i] > largest:
        slargest = largest
        largest = a[i]
    if a[i] > slargest and a[i] < largest:
        slargest = a[i]
print(f'The second largest number in the array is {slargest}')