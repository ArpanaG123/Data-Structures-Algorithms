# To check ith bit is set of not of given number

# Optimal approach
n = 9
i = 2
# output = False
# Explanation: n = 9 -> 1001 , i = 2 as i = 2 is 0

if n & (1<<i) != 0:
    print(True)
else:
    print(False)

# TC = 0(1)
# SC = 0(1)