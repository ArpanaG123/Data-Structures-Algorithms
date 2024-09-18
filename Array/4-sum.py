# 4Sum
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Input: 
nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Link - https://leetcode.com/problems/4sum/description/

# brute force

arr = [1,0,-1,0,-2,2]
target = 0

# output = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

n = len(arr)

res = set()

for a in range(0,n-3):
    for b in range(a+1,n-2):
        for c in range(b+1,n-1):
            for d in range(c+1,n):
                if arr[a] + arr[b] + arr[c] + arr[d] == target:
                    quadruplets = tuple(sorted([arr[a],arr[b],arr[c],arr[d]]))
                    
                    res.add(quadruplets)
                    
                    
result = [list(quad) for quad in res]
print(result)

# TC ~= 0(n^4)
# SC = 0(no. of quad)*2

# Better