# Max Consecutive Ones
# Link - https://leetcode.com/problems/max-consecutive-ones/description/

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

nums = [1,0,1,1,0,1]
# Output: 2

def findMaxConsecutiveOnes(nums):
    n = len(nums)
    count = 0
    mx = 0
    
    for i in range(0,n):
        if nums[i] == 1:
            count += 1
            mx = max(count,mx)
        else:
            count = 0
    return mx
    
result = findMaxConsecutiveOnes(nums)
print(result)