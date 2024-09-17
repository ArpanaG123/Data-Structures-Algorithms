# Check if a number is Armstrong Number or not

# Problem Statement: Given an integer N, return true it is an Armstrong number otherwise return false.
# Link - https://leetcode.com/problems/armstrong-number/description/

# An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

n = 153 
# res = 1^3 + 5^3 + 3^3 = 153 - true

n = 153
original_num = n
sm = 0
while n > 0:
    digit = n % 10
    sm += digit * digit * digit
    n = n//10


if sm == original_num:
    print(True)
else:
    print(False)


# Time Complexity: O(log10N + 1) where N is the input number.