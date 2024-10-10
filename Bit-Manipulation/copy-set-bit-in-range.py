# Copy set bits in a range
# Given two numbers x and y, and a range [l, r] where 1 <= l, r <= 32. The task is consider set bits of y in range [l, r] and set these bits in x also.

# Link - https://www.geeksforgeeks.org/copy-set-bits-in-a-range/

x = 10
y = 13
l = 2
r = 3
# Output : x = 14
# Binary representation of 10 is 1010 and 
# that of y is 1101. There is one set bit
# in y at 3'rd position (in given range). 
# After we copy this bit to x, x becomes 1110
# which is binary representation of 14.

def copySetBit(x,y,l,r):
    if l < 1 or r > 32:
        return x
    
    for i in range(l,r+1):
        bit_mask = 1 <<(i-1)
        
        if bit_mask & y != 0:
            x = x | bit_mask
    return x

x = 10
y = 13
l = 2
r = 3
result = copySetBit(x,y,l,r)
print(result)