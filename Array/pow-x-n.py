# Pow(x, n)
# Link - https://leetcode.com/problems/powx-n/description/

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

x = 2.00000
n = 10
# Output: 1024.00000

x = 2.10000
n = 3
# Output: 9.26100

# Brute force
def myPow(x: float, n: int):
    if n == 0:
        return 1.0
    if n == 1:
        return x
    if n < 0:
        return myPow(1/x,-n)
    
    result = 1
    for i in range(n):
        result = result * x
    return result

x = 2.00000
n = 10
res = myPow(x,n)
print(res)

# TC = 0(n)
# sc = 0(1)

# Optimal
def myPow(x: float, n: int):
    if n == 0:
        return 1.0
    if n == 1:
        return x
    if n < 0:
        return myPow(1/x,-n)
    
    half = myPow(x,n//2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x

x = 2.00000
n = 10
res = myPow(x,n)
print(res)

# TC = 0(logn)
# sc = 0(1)