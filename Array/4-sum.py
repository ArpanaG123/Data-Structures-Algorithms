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

# Better - using hashset

arr = [1,0,-1,0,-2,2]
n = len(arr)
target = 0

res = set()

for i in range(0,n):
    for j in range(i+1,n):
        hashset = set()
        for k in range(j+1,n):
            quad = target - (arr[i] + arr[j] + arr[k])
            
            if quad in hashset:
                quadruplet = sorted([arr[i],arr[j],arr[k],quad])
                res.add(tuple(quadruplet))
            else:
                hashset.add(arr[k])
result = [list(t) for t in res]
print(result)

# TC ~= 0(n^3) * logm - where m is the size of hashset
# SC = 0(no. of quad * 2) + 0(N) - for hashset

# Optimal

arr = [1,0,-1,0,-2,2]
target = 0

arr.sort()

n = len(arr)

res = []

for i in range(0,n):
    if i > 0 and arr[i] == arr[i-1]:
        continue
    
    for j in range(i+1,n):
        if j > i+1 and arr[j] == arr[j-1]:
            continue
        
        k = j+1
        l = n-1
    
        while k < l:
            current_sum = arr[i] + arr[j] + arr[k] + arr[l]
            
            if current_sum < target:
                k += 1
                
            elif current_sum > target:
                l -= 1
                
            else:
                quad = [arr[i], arr[j], arr[k], arr[l]]
                res.append(quad)
                k += 1
                l -= 1
            
                while k < l and arr[k] == arr[k-1]:
                    k += 1
            
                while k < l and arr[l] == arr[l+1]:
                    l -= 1
print(res)
