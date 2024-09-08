#  Concatenation of Consecutive Binary Numbers
# Link - https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/description/

n = 3
# Output: 27
# Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
# After concatenating them, we have "11011", which corresponds to the decimal value 27.

# Brute force

n = 3
res = []

for i in range(1,n+1):
    res.append(bin(i)[2:])
    
binary_str = "".join(res)

# print(binary_str)
m = len(binary_str)

sm = 0
power = 1
for i in range(m-1,-1,-1):
    if binary_str[i] == "1":
        sm = sm + power
    power = power * 2
print(sm)
    

# Optimsed
def concatenatedBinary(self, n: int) -> int:

    binary = ""

    for i in range(1,n+1):
        binary += bin(i)[2:]
        
    res = int(binary,2)

    return res % (10**9 + 7)
