# Problem Statement: Given an integer N, return the number of digits in N.
# Link - https://www.geeksforgeeks.org/problems/count-digits5716/1

# Method1
N = 329823
cnt = 0
while N > 0:
    cnt += 1
    N = N//10

print(cnt)

# TC = 0(logn) - with base10

# Method2
import math

# Calculate the count of digits in 'n'
# using logarithmic operation log10(n) + 1.
def countDigits(n):
    # Initialize a variable 'cnt' to
    # store the count of digits.
    cnt = int(math.log10(n) + 1)

    # The expression int(math.log10(n) + 1)
    # calculates the number of digits in 'n'
    # and casts it to an integer.
    
    # Adding 1 to the result accounts
    # for the case when 'n' is a power of 10,
    # ensuring that the count is correct.
   
    # Finally, the result is cast
    # to an integer to ensure it is rounded
    # down to the nearest whole number.
    
    # Return the count of digits in 'n'.
    return cnt

n = 1234567
res = countDigits(n)
print(res)

# TC = 0(1)