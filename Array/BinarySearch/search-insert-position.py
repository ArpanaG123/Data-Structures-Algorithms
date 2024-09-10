# Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Link - https://leetcode.com/problems/search-insert-position/description/

# Example 1
nums = [1,3,5,6]
target = 5
# Output: 2

# Example 2
nums = [1,3,5,6]
target = 2
# Output: 1

# Approach1 - using linear search
nums = [1,3,5,6]
target = 2
# Output: 1

n = len(nums)

for i in range(0,n):
    if nums[i] == target:
        print(i)
    elif nums[i] > target:
        print(i)
        break
else:
    print(n)

# TC = 0(N)
# SC = 0(1)

# Approach2 - using binary search

nums = [1,3,5,6]
target = 2

n = len(nums)


def serachInsertPosition(nums,target):
    n = len(nums)

    low = 0
    high = n-1

    while low <= high:
        mid = (low+high)//2
    
        if nums[mid] == target:
            return mid
    
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return low

result = serachInsertPosition(nums,target)
print(result)

# TC = 0(logn)
# SC = 0(1)