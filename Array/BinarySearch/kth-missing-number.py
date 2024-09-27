# Kth Missing Positive Number
# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
# Return the kth positive integer that is missing from this array.


arr = [2,3,4,7,11]
k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

# Link - https://leetcode.com/problems/kth-missing-positive-number/description/

# Brute force
arr = [2,3,4,7,11]
k = 5

def findKthPositive(arr,k):
    n = len(arr)
    
    for i in range(0,n):
        if arr[i] <= k:
            k += 1
        else:
            break
    return k
    
res = findKthPositive(arr,k)
print(res)

# Optimal
arr = [2,3,4,7,11]
k = 5

def findKthPositive(arr,k):
    n = len(arr)
    
    low = 0
    high = n-1
    
    while low <= high:
        mid = (low+high)//2
        
        missing_cnt = arr[mid] - (mid + 1)
        
        if missing_cnt < k:
            low = mid + 1
        else:
            high = mid - 1
    # After binary search, the k-th missing number is between arr[high] and arr[low].
    # The number of missing numbers before arr[low] is arr[high] - (high + 1).
    return low + k
    
res = findKthPositive(arr,k)
print(res)

# TC = 0(logn)