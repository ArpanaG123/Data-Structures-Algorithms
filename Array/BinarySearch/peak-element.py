# Find Peak Element
# lINK - https://leetcode.com/problems/find-peak-element/description/

nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Brute force - using linear search
arr = [1,2,3,4,5,6,7,8,5,1]

def findPeakElement(arr):
    n = len(arr)

    for i in range(0,n):
        if ((i == 0 or arr[i-1] < arr[i]) and (i == n-1 or arr[i] > arr[i+1])):
            return i
    else:
        return -1

res = findPeakElement(arr)
print(res)
# TC = 0(N)
# SC = 0(1)

# Optimal - using binary search

arr = [1,2,3,4,5,6,7,8,5,1]

def findPeakElement(arr):
    n = len(arr)
    
    if n == 1:
        return 0
    
    if arr[0] > arr[1]:
        return 0
    
    if arr[n-1] > arr[n-2]:
        return n-1
        
    low = 1
    high = n-2
    
    while low <= high:
        
        mid = (low + high)//2
        
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid] > arr[mid-1]:
            low = mid + 1
        elif nums[mid] > nums[mid+1]:
            high = mid - 1
        else:
            low = mid + 1
    
    return - 1

res = findPeakElement(arr)
print(res)

# TC = 0(logN)
# SC = 0(1)