# Problem Statement: Given an integer N return the reverse of the given number.
# Note: If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.
# Link - https://leetcode.com/problems/reverse-integer/description/

# case1 - n = 10400

# case2 - n = 123

# case3 - n = -123

n = 120
n = 123
n = -123

rev = 0
original_num = n
num = abs(n)

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num//10

if n < 0:
    rev = -rev

# Check for 32-bit overflow
if rev < -2**31 or rev > 2**31 - 1:
    print(0)

print(rev)


# Time Complexity: O(log10N + 1) where N is the input number