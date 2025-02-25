# Determining the Length of a String Without Using Built-In Functions

string = input('Enter string:')
length = 0
for char in string:
    length += 1
print(f'The length of the string is {length}')
