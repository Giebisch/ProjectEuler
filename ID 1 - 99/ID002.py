# Solved ! Solution correct.

# Even Fibonacci numbers

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

fib_numbers = [1, 2]

def get_fibonacci_numbers(max_number):
    global fib_numbers
    number_one = 1
    number_two = 2
    for i in range(1, max_number):
        new_number = number_one + number_two
        number_one = number_two
        number_two = new_number
        fib_numbers.append(number_two)
        if number_two >= max_number:
            break
def sum_even_fib_numbers(max_number):
    global fib_numbers
    get_fibonacci_numbers(max_number)
    even_numbers = [x for x in fib_numbers if x % 2 == 0]
    return sum(even_numbers)

if __name__ == "__main__":
    print(sum_even_fib_numbers(4000000)) #4613732