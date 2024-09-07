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

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handling the special case where dividend equals divisor
        if dividend == divisor:
            return 1

        # Handle overflow for edge case INT_MIN divided by -1
        INT_MAX = (1 << 31) - 1
        INT_MIN = -(1 << 31)
        
        # Handle overflow case for INT_MIN divided by -1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1

        # Use absolute values for calculation
        n = abs(dividend)
        d = abs(divisor)

        ans = 0

        # Keep subtracting divisor (shifted by powers of 2) from dividend
        while n >= d:
            cnt = 0
            # Shift the divisor left until it's smaller than n
            while n >= (d << (cnt + 1)):  # Corrected the inner while condition
                cnt += 1
            
            # Subtract the shifted divisor from n
            n -= d << cnt
            # Add the corresponding power of 2 to ans
            ans += 1 << cnt

        # Apply the sign to the final result
        return sign * ans

# Example usage:
solution = Solution()
result = solution.divide(22, 3)
print(result)  # Output will be the integer division of 22 by 3

