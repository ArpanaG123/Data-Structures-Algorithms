# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Link - https://leetcode.com/problems/3sum/description/

 

# Example 1:
# Input: 
nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Brute force

arr = [-1,0,1,2,-1,-4]
def threeSum(arr):
    n = len(arr)
    
    res = []
    
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplet = sorted([arr[i],arr[j],arr[k]])
                    
                    if triplet not in res:
                        res.append(triplet)
    
    return res
    
result = threeSum(arr)
print(result)

# TC = 0(N^3)*nlogn
# SC = O(2 * no. of the unique triplets) 

# Better - using hashing

arr = [-1,0,1,2,-1,-4]
def threeSum(arr):
    n = len(arr)
    
    res = set()
    for i in range(0,n):
        hashset = set()
        for j in range(i+1,n):
            third = -(arr[i] + arr[j])
            
            if third in hashset:
                triplet = sorted([arr[i], arr[j], third])
                res.add(tuple(triplet))
            else:
                hashset.add(arr[j])
                
    return [list(t) for t in res]
            
result = threeSum(arr)
print(result)

# TC = 0(N^2)*nlogn
# SC = O(2 * no. of the unique triplets) 

# Optimal - using two pointer

arr = [-2,0,1,1,2]
def threeSum(arr):
    arr.sort()
    n = len(arr)
    
    res = []
    for i in range(0,n):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        j = i+1
        k = n-1
        
        while j < k:
            sm = arr[i] + arr[j] + arr[k]
            
            if sm < 0:
                j += 1
            elif sm > 0:
                k -= 1
            else:
                triplet = [arr[i],arr[j],arr[k]]
                res.append(triplet)
                j += 1
                k -= 1
                while j < k and arr[j] == arr[j - 1]:
                    j += 1
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1
            
    return res
            
result = threeSum(arr)
print(result)