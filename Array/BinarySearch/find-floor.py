# Floor in a Sorted Array
# Link - https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1?track=DSASP-Searching&amp%253BbatchId=154&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=floor-in-a-sorted-array

# Given a sorted array arr[] of size n without duplicates, and given a value x. Floor of x is defined as the largest element k in arr[] such that k is smaller than or equal to x. Find the index of k(0-based indexing).


# Examples
x = 0 
arr = [1,2,8,10,11,12,19]
# Output: -1
# Explanation: No element less than 0 is found. So output is "-1".

x = 5 
arr = [1,2,8,10,11,12,19]
# Output: 1
# Explanation: Largest Number less than 5 is 2 (i.e k = 2), whose index is 1(0-based indexing).

arr = [1,2,8,10,11,12,19]
x = 0

def find_floor(arr,x):
    n = len(arr)
    
    low = 0
    high = n-1
    
    ans = -1
    
    while low <= high:
        mid = (low + high)//2
        
        if arr[mid] <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return ans
    
result = find_floor(arr,x)
print(result)

# TC = 0(Logn)
# SC = 0(1)