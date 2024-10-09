# Find subsets
# Link - https://leetcode.com/problems/subsets/description/

nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

nums = [1,2,3]
n = len(nums)

total_subset = 1<<n
ans = []

for i in range(0,total_subset):
    subsets = []
    
    for num in range(0,n):
        if i & (1<<num):
            subsets.append(nums[num])
    ans.append(subsets)
print(ans)

# TC = 0(N * 2^N)

# Type2
nums = "abc"
n = len(nums)

total_subset = 1 << n  # Total number of subsets
ans = []

for i in range(1, total_subset):  # Start from 1 to avoid the empty subset
    subsets = ""
    for j in range(n):
        if i & (1 << j):  # Check if the num-th bit is set in i
            subsets += nums[j]
    ans.append(subsets)  # Join characters to form the subset string
ans.sort()

print(ans)  

# sum of xor of all subsets

nums = [1,5,6]

n = len(nums)
total = 1<<n
sm = 0

for i in range(total):
    curr = 0
    for j in range(n):
        if i & (1<<j):
            curr = curr ^ nums[j]
    sm += curr
print(sm)