# Solved! Solution correct.

# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

def get_largest_prime(number):
    original_number = number
    count = 2
    prime_factors = []
    while count < math.sqrt(original_number):
        if (number / count).is_integer():
            number = number / count
            prime_factors.append(count)
        else:
            count += 1
    return max(prime_factors)

if __name__ == "__main__":
    print(get_largest_prime(600851475143))