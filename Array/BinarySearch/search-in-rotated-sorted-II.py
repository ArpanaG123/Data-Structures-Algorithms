# Search in rotated sorted array II.
# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# link - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

# Example 1:
nums = [2,5,6,0,0,1,2]
target = 0
# Output: true

# Example 2:
nums = [2,5,6,0,0,1,2]
target = 3
# Output: false

def search(nums,target):
    n = len(nums)
    low = 0
    high = n-1

    while low <= high:
        mid = (low+high)//2

        if nums[mid] == target:
            return True
        
        # If the elements at 'low', 'mid', and 'high' are all the same,
        # we cannot determine the sorted part, so we reduce the search space
        # by moving both pointers inward
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1  
        elif nums[low] <= nums[mid]:
            if nums[low] <= target and target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        
    return False
    
nums = [2,5,6,0,0,1,2]
target = 0  
result = search(nums,target)
print(result)

# TC = 0(log n)
# SC = 0(1)