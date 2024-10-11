# Minimum Flips to Make a OR b Equal to c
# Link - https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description/

# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

# Example 1
a = 2
b = 6
c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

def minFlips(a,b,c):
    
    flips = 0
    
    while a > 0 or b > 0 or c > 0:
        bit_a = a & 1
        bit_b = b & 1
        bit_c = c & 1
        
        if bit_c == 0:
            flips += (bit_a + bit_b)
        else:
            if bit_a == 0 and bit_b == 0:
                flips += 1
        
        a = a>>1
        b = b>>1
        c = c>>1
        
    return flips

a = 2
b = 6
c = 5
result = minFlips(a,b,c)
print(result)