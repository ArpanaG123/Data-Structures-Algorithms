#  Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:
x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

def mySqrt(x):

    low = 0
    high = x

    ans = -1

    while low <= high:

        mid = (low + high)//2

        if mid * mid == x:
            return mid

        elif mid * mid > x:
            high = mid - 1
            
        else:
            ans = mid
            low = mid + 1
        
    return ans

result = mySqrt(x)
print(result)

# TC = 0(logn)
# SC = 0(1)
        