# Identifying Palindromes

str1 = input('enter string:')
new_str = str1[::-1]
if str1 == new_str:
    print(f'{str1} is pallindrome')
else:
        print(f'{str1} is not pallindrome')

