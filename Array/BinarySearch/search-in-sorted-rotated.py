# Search in Rotated Sorted Array
# Link - https://leetcode.com/problems/search-in-rotated-sorted-array/description/

nums = [4,5,6,7,0,1,2]
target = 0
# Output: 4

def searchInsortedArray(nums,target):
    n = len(nums)
    
    low = 0
    high = n-1
    
    while low <= high:
        mid = (low + high)//2
        
        if nums[mid] == target:
            return mid
        
        if nums[low]  <= nums[mid]:
            if (nums[low] <= target and target <= nums[mid]):
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
result = searchInsortedArray(nums,target)
print(result)

# TC = 0(logn)
# SC = 0(1)