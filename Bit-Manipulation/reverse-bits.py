# Reverse Bits
# Link - https://leetcode.com/problems/reverse-bits/

s = "00000010100101000001111010011100"
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

# Method1 - Brute force

s = "00000010100101000001111010011100"

n = len(s)
bits = list(s)
sz = len(bits)

res = []
for i in range(n-1,-1,-1):
    res.append(bits[i])

# print("".join(res))

l = len(res)
pow = 1
ans = 0
for i in range(l-1,-1,-1):
    if res[i] == "1":
        ans = ans + pow
    pow = pow * 2
print(ans)

# TC = 0(n)
# Reversing the string (which is an 0(N) operation)
# Iterating over the reversed string to calculate the decimal value (also an  O(n) operation).
# SC = 0(n) - to store rev bits in res

# Method2 - Optimal approach

# Points
# 1.iterate from 0,32 bits
# 2.check if ith bit is set bit then placed that bit in its correct order in reverse order.else
# 3.And then return the answer

n = "00000010100101000001111010011100"

# converting it into string as above is in string but in code it is given a unsigned interger so no need of conversion.
num = int(n,2)

ans = 0
for i in range(0,32):
    if num & (1<<i):
        ans = ans | 1 << (32-i-1)
print(ans)


