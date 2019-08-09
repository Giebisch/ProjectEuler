# Solved ! Solution correct.

# Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def is_evenly_divisible(max_number, number):
    for i in range(1, max_number + 1):
        if number % i != 0:
            return False
    return True

def get_smallest_multiple(number):
    i = 0
    while True:
        if is_evenly_divisible(number, i) and i != 0:
            break
        else:
            i += 20 # has to be divisible by 20
    return i

if __name__ == "__main__":
    print(get_smallest_multiple(20)) #232792560