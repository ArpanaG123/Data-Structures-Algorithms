#  Single Element in a Sorted Array
# Link - https://leetcode.com/problems/single-element-in-a-sorted-array/description/

# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.

nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

# Brute force

arr = [1,1,2,3,3,4,4,8,8]
n = len(arr)

if n == 1:
    print(arr[0])
for i in range(0,n):
    if i == 0:
        if arr[i] != arr[i+1]:
            print(arr[i])
    elif i == n-1:
        if arr[i] != arr[i-1]:
            print(arr[i])
    else:
        if arr[i] != arr[i+1] and arr[i] != arr[i-1]:
            print(arr[i])

# TC = 0(N)

# Using binary search

arr = [3,3,7,7,10,11,11]

def searchSingleElement(arr):
    n = len(arr)
    
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    low = 1
    high = n-2
    
    while low <= high:
        mid = (low+high)//2
        
        if arr[mid] != arr[mid+1] and arr[mid] != arr[mid-1]:
            return arr[mid]
        if mid % 2 == 1:
            if arr[mid] == arr[mid-1]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if arr[mid] == arr[mid+1]:
                low = mid + 2
            else:
                high = mid - 2
            
result = searchSingleElement(arr)
print(result)