# Checking for an Anagram

string1 = input('Enter first string:')
string2 = input('Enter second string:')

sorted_string1 = sorted(string1)
sorted_string2 = sorted(string2)

if sorted_string1 == sorted_string2:
    print(True)
else:
    print(False)
