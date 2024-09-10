# Binary search
# Link - https://leetcode.com/problems/binary-search/description/

# Example1
nums = [-1,0,3,5,9,12]
target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example2
nums = [-1,0,3,5,9,12]
target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Approach1 - using linear search
nums = [-1,0,3,5,9,12]
target = 9

n = len(nums)

for i in range(0,n):
    if nums[i] == target:
        print(i)
        break

# TC = 0(N)
# SC = 0(1)

# Approach2 - using binary search

nums = [-1,0,3,5,9,12]
target = 9

def serachElement(nums,target):
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
    
    return -1

result = serachElement(nums,target)
print(result)

# TC = 0(logn)
# SC = 0(1)