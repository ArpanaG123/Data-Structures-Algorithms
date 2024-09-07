# To clear ith bit of given number.

# Optimal approach
n = 13
i = 2
# output = 9
# Explanation: n = 13 -> 1101 , i = 2 which is now 1001

print(n & ~(1<<i))

# TC = 0(1)
# SC = 0(1)