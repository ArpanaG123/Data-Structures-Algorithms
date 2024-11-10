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

def findMininmumInRotatedSorted(arr, n):
    # Initialize two pointers:
    # 'low' starts at the beginning of the array
    # 'high' starts at the end of the array
    low = 0
    high = n - 1
    
    # We continue searching as long as 'low' is less than 'high'
    while low < high:
        # Calculate the middle index by averaging 'low' and 'high'
        mid = (low + high) // 2

        # If the middle element is greater than the element at 'high',
        # this means the smallest element is in the right half
        if arr[mid] > arr[high]:
            # Move 'low' to the right of 'mid' since the minimum must be
            # somewhere after 'mid'
            low = mid + 1
        else:
            # If 'arr[mid]' is less than or equal to 'arr[high]', it means the
            # smallest element is in the left half (including 'mid')
            high = mid
    
    # When the loop ends, 'low' will point to the smallest element
    return arr[low]

# Example usage:
arr = [4, 5, 6, 7, 0, 1, 2]  # A rotated sorted array
n = len(arr)

# Call the function to find the minimum element in the rotated sorted array
result = findMininmumInRotatedSorted(arr, n)
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