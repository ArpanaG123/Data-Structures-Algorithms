# Number of occurrence
# Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.

# Link - https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number-of-occurrence


# Input:
x = 2
Arr = [1, 1, 2, 2, 2, 2, 3]
# Output: 4
# Explanation: x = 2 occurs 4 times in the given array so the output is 4.

nums = [1, 1, 2, 2, 2, 2, 3]
target = 4

def firstOccurence(nums,target):
    n = len(nums)
    
    low = 0
    high = n-1
    
    ans = -1
    
    while low <= high:
        mid = (low + high)//2
        
        if nums[mid] == target:
            ans = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return ans
    
def lastOccurence(nums,target):
    n = len(nums)
    
    low = 0
    high = n-1
    
    ans = -1
    
    while low <= high:
        mid = (low + high)//2
        
        if nums[mid] == target:
            ans = mid
            low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return ans

def CountOccurence(nums,target):
    
    first = firstOccurence(nums,target)
    last = lastOccurence(nums,target)
    
    if first == -1:
        return 0
    
    count = last - first + 1
    
    return count

    
result = CountOccurence(nums,target)
print(result)