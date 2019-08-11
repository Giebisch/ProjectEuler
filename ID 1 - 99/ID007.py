# Solved ! Solution correct.

# 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math

def check_if_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if (number % i) == 0:
            return False
    return True

def get_primes():
    prime_numbers = [2, 3, 5, 7, 11, 13]
    counter = 14
    while len(prime_numbers) < 10001:
        if check_if_prime(counter):
            prime_numbers.append(counter)
        counter += 1
    print(prime_numbers[-1]) #print 10001th prime

if __name__ == "__main__":
    get_primes() #104743