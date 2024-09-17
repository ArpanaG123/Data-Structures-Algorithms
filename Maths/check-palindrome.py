# Check if a number is Palindrome or Not

# Problem Statement: Given an integer N, return true if it is a palindrome else return false.
# Link - https://leetcode.com/problems/palindrome-number/description/

num = -121
original_num = num
rev = 0

if num < 0:
    print(False)

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num//10

if rev == original_num:
    print(True)
else:
    print(False)

# Time Complexity: O(log10N + 1) where N is the input number

