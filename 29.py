# Finding the Largest Palindrome in a String

string = "babad"
n = len(string)
longest = ""

for i in range(n):
    for j in range(i, n):
        substring = string[i:j+1]  
        if substring == substring[::-1] and len(substring) > len(longest):
            longest = substring  

print(longest)
