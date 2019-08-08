# Solved ! Solution correct.

# Multiples of 3 and 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def get_sum_below(max_number):
    accepted_numbers = []
    for i in range(1, max_number):
        for j in [3, 5]:
            if (i/j).is_integer():
                accepted_numbers.append(i)
                break
    return sum(accepted_numbers)

if __name__ == "__main__":
    print(get_sum_below(1000)) #233168