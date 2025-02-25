# Finding the Mode of Numbers in an Array

array = [1, 2, 2, 3, 4, 4, 4]
mode = array[0]
max_count = 0
for num in array:
    count = 0  
    for element in array:
        if element == num:
            count += 1
    
    if count > max_count:
        max_count = count
        mode = num
print(f'The most frequent number in the array is {mode}')
