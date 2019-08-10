# Solved ! Solution correct.

# Sum square difference

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def square_of_sums():
    sum_numbers = sum([x for x in range(1,101)])
    return sum_numbers**2

def sum_of_squares():
    squares = [x**2 for x in range(1,101)]
    return sum(squares)

if __name__ == "__main__":
    print(int(square_of_sums() - sum_of_squares())) #25164150