# Checking for Perfect Squares

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i * i == n:
        print(f"{n} is a perfect square.")
        break
else:
    print(f"{n} is not a perfect square.")

