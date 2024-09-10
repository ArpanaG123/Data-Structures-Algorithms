# Find First and Last Position of Element in Sorted Array
# Link - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

# Example 1:
# Input:
nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

nums = [5,7,7,8,8,10]
target = 8
# Output: [3,4]

def firstOccurence(nums,target):
    n = len(nums)
    
    low = 0
    high = n-1
    ans = -1
    while low <= high:
        m = (low+high)//2
        
        if nums[m] == target:
            ans = m
            high = m - 1
        elif nums[m] < target:
            low = m + 1
        else:
            high = m-1
            
    return ans

def lastOccurence(nums,target):
    n = len(nums)
    
    low = 0
    high = n-1
    ans = -1
    while low <= high:
        m = (low+high)//2
        
        if nums[m] == target:
            ans = m
            low = m + 1
        elif nums[m] < target:
            low = m + 1
        else:
            high = m-1
            
    return ans

def searchRange(nums,target):
    res = [0]*2
    
    start = firstOccurence(nums,target)
    end = lastOccurence(nums,target)
    
    res[0] = start
    res[1] = end
    
    return res

result = searchRange(nums,target)
print(result)