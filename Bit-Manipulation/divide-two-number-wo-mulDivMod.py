# Divide Two Integers
# Link - https://leetcode.com/problems/divide-two-integers/description/

# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

dividend = 10
divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.

# Approach1

sm = 0
cnt = 0

while sm+divisor <= dividend:
    cnt += 1
    sm += divisor
print(cnt)

# TC = 0(dividend)
# SC = 0(1)

# Approach2
def divide(dividend,divisor):
    if divisor == dividend:
        return 1
    
    # Handle overflow case for INT_MIN divided by -1
    if dividend == -(1<<31) and divisor == -1:
        return (1<<31) - 1
    
    sign = 1
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        sign = -1
    
    n = abs(dividend)
    d = abs(divisor)
    ans = 0

    # Keep subtracting divisor (shifted by powers of 2) from dividend
    while n >= d:
        cnt = 0

        # Shift the divisor left until it's smaller than n
        while n >= (d<<(cnt+1)):
            cnt += 1
        
        # Subtract the shifted divisor from n
        n = n - (d<<cnt)
        # Add the corresponding power of 2 to ans
        ans = ans + (1<<cnt)

    # Apply the sign to the final result
    return ans * sign

# Example usage:   
dividend = 22
divisor = 3
result = divide(dividend,divisor)
print(result)
# output = 22//3 = 7

