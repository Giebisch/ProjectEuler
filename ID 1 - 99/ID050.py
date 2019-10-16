# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13

# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import math

prime_numbers = [2]
def check_if_prime(number):
    if number < 2:
        return False
    for i in range(2, math.floor(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def get_prime_numbers():
    global prime_numbers
    for i in range(3, 1000000):
        if check_if_prime(i) == True:
            prime_numbers.append(i)

def get_number():
    global prime_numbers
    result = 0
    count_record = 0
    for i, prime in enumerate(prime_numbers):
        te = 0
        count = 0
        while te < 1000000 and (count + i) < len(prime_numbers) - 1:
            te += prime_numbers[count + i]
            count += 1
            if check_if_prime(te) == True:
                if count > count_record:
                    count_record = count
                    result = te
    return result

if __name__ == "__main__":
    get_prime_numbers()
    print(get_number()) #Result 9977651