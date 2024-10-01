# String to Integer (atoi)
# Link - https://leetcode.com/problems/string-to-integer-atoi/description/

# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:
# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.


s = "  -4123abde0"
s = "42"
# output = -4123
# Output = 42

def myAtoi(s):
    
    n = len(s)
    
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    
    if n == 0:
        return 0
    
    ans = 0
    sign = 1
    
    i = 0
    
    while i < n and s[i] == " ":
        i += 1
        
    if i < n and (s[i] == '-' or s[i] == '+'):
        if s[i] == '-':
            sign = -1
        else:
            sign = 1
            
        i += 1
    
    while i < n and s[i].isdigit():
        ans = ans * 10 + int(s[i])
        i += 1
    
    ans * sign
    
    if ans < INT_MIN:
        return INT_MIN
        
    if ans > INT_MAX:
        return INT_MAX
        
    return ans
    
result = myAtoi(s)
print(result)