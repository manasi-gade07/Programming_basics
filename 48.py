
number = 12
sum_of_prime_factors = 0
i = 2

while i <= number:
    if number % i == 0:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            sum_of_prime_factors += i
        number = number // i
    else:
        i += 1

print(sum_of_prime_factors)
