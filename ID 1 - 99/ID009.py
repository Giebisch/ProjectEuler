

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def check_if_pyth(a, b, c):
    if (a**2 + b**c) == c**2:
        return True
    return False

def get_product():
    for c in range(200, 1000):
        print(c)
        for b in range(0, c):
            for a in range(0, c):
                if check_if_pyth(a, b, c) and (a + b + c) == 1000:
                    return a*b*c

if __name__ == "__main__":
    print(get_product())