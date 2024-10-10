# Find position of set bit
# Given a number N having only one ‘1’ and all other ’0’s in its binary representation, find position of the only set bit. If there are 0 or more than 1 set bit the answer should be -1. Position of  set bit '1' should be counted starting with 1 from LSB side in binary representation of the number.
# Link - https://www.geeksforgeeks.org/problems/find-position-of-set-bit3706/1

# N = 2
# Output:2
# Explanation:
# 2 is represented as "10" in Binary.
# As we see there's only one set bit
# and it's in Position 2 and thus the
# Output 2.

# Brute force
n = 12

def findPositionOfSetbit(n):
    bit = bin(n)[2:]
    
    sz = len(bit)
    
    for i in range(sz-1,-1,-1):
        if bit[i] == "1":
            return (sz-i)
            
result = findPositionOfSetbit(n)
print(result)

# Optimal
n = 12

def findPositionOfSetbit(n):
    if n == 0:
        return -1
    
    pos = 1
    while n & 1 == 0:
        n = n>>1
        pos += 1
    return pos
            
result = findPositionOfSetbit(n)
print(result)