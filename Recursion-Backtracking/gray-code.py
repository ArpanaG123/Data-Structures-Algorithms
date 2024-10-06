# Gray Code
# Link - https://leetcode.com/problems/gray-code/description/

# An n-bit gray code sequence is a sequence of 2n integers where:
# Every integer is in the inclusive range [0, 2n - 1],
# The first integer is 0,
# An integer appears no more than once in the sequence,
# The binary representation of every pair of adjacent integers differs by exactly one bit, and
# The binary representation of the first and last integers differs by exactly one bit.
# Given an integer n, return any valid n-bit gray code sequence.

n = 2
# Output: [0,1,3,2]

# Explanation:
# The binary representation of [0,1,3,2] is [00,01,11,10].
# - 00 and 01 differ by one bit
# - 01 and 11 differ by one bit
# - 11 and 10 differ by one bit
# - 10 and 00 differ by one bit
# [0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
# - 00 and 10 differ by one bit
# - 10 and 11 differ by one bit
# - 11 and 01 differ by one bit
# - 01 and 00 differ by one bit

# Type1
def grayCode(n):
    if n == 0:
        return ["0"]
    
    if n == 1:
        return ["0","1"]
        
    res = []
        
    prev_code = grayCode(n-1)
    
    for code in prev_code:
        res.append("0" + code)
    
    for code in reversed(prev_code):
        res.append("1" + code)
        
    return res
    

n = 3
result = grayCode(n)
print(result)
# output - ['000', '001', '011', '010', '110', '111', '101', '100']

# Type2
def grayCode(n):
    if n == 0:
        return [0]
    
    if n == 1:
        return [0,1]
        
    res = []
        
    prev_code = grayCode(n-1)
    
    for code in prev_code:
        res.append(code)

    for code in reversed(prev_code):
        res.append((1<<(n-1)) + code)
        
    return res
    

n = 3
result = grayCode(n)
print(result)
# output = [0, 1, 3, 2, 6, 7, 5, 4]