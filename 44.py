# Finding the Average of Numbers in an Array

array = [1, 2, 3, 4, 5]
total_sum = 0
for num in array:
    total_sum += num
average = total_sum // len(array)
print(f'The average of the numbers is {average}')
