# To set ith bit of given number

# Optimal approach
n = 9
i = 2
# output = 13
# Explanation: n = 9 -> 1001 , i = 2 which is now 1101

print(n | (1<<i))

# TC = 0(1)
# SC = 0(1)