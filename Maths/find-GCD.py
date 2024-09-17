# Find GCD of two numbers.GCD or HCF - same
# Problem Statement: Given two integers N1 and N2, find their greatest common divisor.

# Link - https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1

# Highest or greatest common divisors

# Brute force
a = 20
b = 15

n = min(a,b)

factors = []
for i in range(1,n+1):
    if a % i == 0 and b % i == 0:
        factors.append(i)
print(max(factors))

# TC = 0(min(a,b))
# sc = 0(1)

# Optimal approach
# Euclidean algorithm

# The Euclidean Algorithm is a method for finding the greatest common divisor of two numbers. 
# It operates on the principle that the GCD of two numbers remains the same even if the smaller number is subtracted from the larger number.
# gcd(a,b) = gcd(a-b,b)
# To find the GCD of n1 and n2 where n1 > n2:
# Repeatedly subtract the smaller number from the larger number until one of them becomes 0.
# Once one of them becomes 0, the other number is the GCD of the original numbers.
a = 20
b = 15
def find_gcd(a, b):
    # Continue loop as long as both
    # a and b are greater than 0
    while a > 0 and b > 0:
        # If a is greater than b,
        # subtract b from a and update a
        if a > b:
            # Update a to the remainder
            # of a divided by b
            a = a % b
        # If b is greater than or equal
        # to a, subtract a from b and update b
        else:
            # Update b to the remainder
            # of b divided by a
            b = b % a
    # Check if a becomes 0,
    # if so, return b as the GCD
    if a == 0:
        return b
    # If a is not 0,
    # return a as the GCD
    return a


gcd = find_gcd(a,b)
print(f"GCD of {a} and {b} is: {gcd}")

# Time Complexity: O(min(N1, N2)) where N1 and N2 is the input number. 

# LCM = a*b//gcd
