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

# Topic - recusion and backtracking

def greyCode(n):
    if n == 0:
        return [0]
    
    if n == 1:
        return [0,1]
    
    res = []

    prev_code = greyCode(n-1)

    for code in prev_code:
        res.append(code)

    for code in reversed(prev_code):
        res.append((1<<(n-1))+code)

    return res

result = greyCode(n)
print(result)