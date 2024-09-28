# Split Array Largest Sum
# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
# Return the minimized largest sum of the split.
# A subarray is a contiguous part of the array.


nums = [7,2,5,10,8]
k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

# Optimal  - using binary search

arr = [7,2,5,10,8]
k = 2

def findPartitions(arr,maxSum):
    n = len(arr)
    partitions = 1
    subarraySum = 0
    
    for i in range(n):
        if subarraySum + arr[i] <= maxSum:
            subarraySum += arr[i]
        else:
            partitions += 1
            subarraySum = arr[i]
    
    return partitions
            
    
def splitArray(arr,k):
    low = max(arr)
    high = sum(arr)
    
    while low <= high:
        mid = (low+high)//2
        
        partitionCount = findPartitions(arr,mid)
        
        if partitionCount > k:
            low = mid + 1
        else:
            high = mid - 1
            
    return low
    
res = splitArray(arr,k)
print(res)
