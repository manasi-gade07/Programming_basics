# Finding Missing Numbers in a Sequence

sequence = [1, 2, 4, 5]
n = max(sequence)
missing_number = []
for num in range(1,n+1):
    if num not in sequence:
        missing_number.append(num)
print(f'The missing number in the sequence from 1 to {n} is {missing_number}')