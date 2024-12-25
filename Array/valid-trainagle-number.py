# Valid Triangle Number
# Link - https://leetcode.com/problems/valid-triangle-number/description/

# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.


nums = [2,2,3,4]
# Output: 3
# Explanation: 
# Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3

nums = [4,2,3,4]
# Output: 4

# Approach1 - brute force

nums = [2, 2, 3, 4]

cnt = 0
n = len(nums)

for i in range(0,n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if nums[i] + nums[j] > nums[k]:
                cnt += 1

print(cnt)  # Output: 3

# TC = 0(N^3)
# SC = 0(1)

# Approach2 - Two pointer

def triangleNumber(nums):
    n = len(nums)

    nums.sort()
    cnt = 0

    for i in range(n-1,-1,-1):
        low = 0
        high = i-1

        while low < high:
            if nums[low] + nums[high] > nums[i]:
                cnt += (high - low)  
                high -= 1
            else:
                low += 1
    return cnt

nums = [2,2,3,4]
result = triangleNumber(nums)
print(result)