# Find XOR of numbers from L to R.
# Link - https://www.geeksforgeeks.org/problems/find-xor-of-numbers-from-l-to-r/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-xor-of-numbers-from-l-to-r


L = 4
R = 8 
# Output:8 
# Explanation:
# 4 ^ 5 ^ 6 ^ 7 ^ 8 = 8

# Approach1
l = 4
r = 8
ans = 0
for i in range(l,r+1):
    ans = ans ^ i
print(ans)

# Approach2

def findXOR(l, r):
    # Function to calculate XOR from 0 to x
    def xor_upto(x):
        if x % 4 == 0:
            return x
        elif x % 4 == 1:
            return 1
        elif x % 4 == 2:
            return x + 1
        else:
            return 0
    
    # XOR from l to r is XOR(0 to r) ^ XOR(0 to l-1)
    return xor_upto(r) ^ xor_upto(l - 1)

# Example usage:
print(findXOR(3, 6))  # Output: 5
