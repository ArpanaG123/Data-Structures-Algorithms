# Find Minimum in Rotated Sorted Array

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# For example, the array nums = [0,1,2,4,5,6,7] might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.

nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Link - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/


# Approach - using Binary search

arr = [4,5,6,7,8,9,1,2,3]
n = len(arr)

def findMininmumInRotatedSorted(arr,n):
    
    low = 0
    high = n-1
    
    while low < high:
        mid = (low + high)//2

        
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    
    return arr[low]

result = findMininmumInRotatedSorted(arr,n)
print(result)

# TC = 0(logN)
# SC = 0(1)

# Type2 - with dupliactes

# Link - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

arr = [2,2,2,0,1]
n = len(arr)

def findMininmumInRotatedSortedII(arr,n):
    
    low = 0
    high = n-1
    
    while low < high:
        mid = (low + high)//2

        if arr[mid]  == arr[high]:
            high -= 1

        elif arr[mid] > arr[high]:
            low = mid + 1

        else:
            high = mid
    
    return arr[low]

result = findMininmumInRotatedSortedII(arr,n)
print(result)