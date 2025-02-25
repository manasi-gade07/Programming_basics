# Counting Vowels and Consonants in a String

a = input('Enter string:')
vowels_set = "aeiouAEIOU"  
vowel = 0
cons = 0

for ch in a:
    if ch in vowels_set:  
        vowel += 1
    elif ch.isalpha():  
        cons += 1

print(f'Vowels: {vowel}, Consonants: {cons}')
