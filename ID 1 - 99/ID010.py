# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

primes = [1]

def check_if_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

for i in range(3, 2*10**6, ):
    print(i)
    if check_if_prime(i):
        primes.append(i)

print(sum(primes))