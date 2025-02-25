# Finding the Median of an Array

array = [3, 1, 2, 4, 5]
array.sort()
n = len(array)
if n % 2 == 1:
    
    median = array[n // 2]
else:
    median = (array[n // 2 - 1] + array[n // 2]) / 2

print(median)
