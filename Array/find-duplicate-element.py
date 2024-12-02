# Find the Duplicate Number
# Link - https://leetcode.com/problems/find-the-duplicate-number/description/


# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and using only constant extra space.

# Input: nums = [1,3,4,2,2]
# Output: 2

# Input: nums = [3,1,3,4,2]
# Output: 3

# Approach1 - Brute force

def findDuplicate(nums):
 
    n = len(nums)
    
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] == nums[i]:
                count += 1
        if count > 1:
            return nums[i]

nums = [3,1,3,4,2]
result = findDuplicate(nums)
print(result)

# TC = 0(N^2)
# SC = 0(1)

# Approach2 - Better using hashing

def findDuplicate(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for k,v in freq.items():
        if v >= 2:
            return k

nums = [3,1,3,4,2]
result = findDuplicate(nums)
print(result)

# TC = 0(N)
# SC = 0(N)


# Approach3 - Optimal

def findDuplicate(nums):
    nums.sort()
    n = len(nums)
    
    for i in range(1,n):
        if nums[i] == nums[i-1]:
            return nums[i]

nums = [3,1,3,4,2]
result = findDuplicate(nums)
print(result)

# TC = 0(NlogN)
# SC = 0(1)