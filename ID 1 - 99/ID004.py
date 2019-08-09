# Solved ! Solution correct.

# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def check_if_palindrome(number):
    number_as_string = str(number)
    if number_as_string == number_as_string[::-1]:
        return True
    else:
        return False

def largest_palindrome():
    palindromes = []
    for i in range(0,1000):
        for j in range(0,1000):
            if check_if_palindrome(j*i):
                palindromes.append(i*j)
    return max(palindromes)

if __name__ == "__main__":
    print(largest_palindrome()) #906609