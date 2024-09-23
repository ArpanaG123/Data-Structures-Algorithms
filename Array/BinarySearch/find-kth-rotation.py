# Find Kth Rotation
# Link - https://www.geeksforgeeks.org/problems/rotation4723/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=rotation


# Given an increasing sorted rotated array arr of distinct integers. The array is right-rotated k times. Find the value of k.
# Let's suppose we have an array arr = [2, 4, 6, 9], so if we rotate it by 2 times so that it will look like this:
# After 1st Rotation : [9, 2, 4, 6]
# After 2nd Rotation : [6, 9, 2, 4]

# Examples:
arr = [5, 1, 2, 3, 4]
# Output: 1
# Explanation: The given array is 5 1 2 3 4. The original sorted array is 1 2 3 4 5. We can see that the array was rotated 1 times to the right

def findKthRotation(arr):
    n = len(arr)
    
    low = 0
    high = n-1
    
    
    while low < high:
        mid = (low + high)//2
        
        if arr[mid] > arr[high]:
            low = mid+1
        else:
            high = mid
    
    return low

arr = [3,4,5,1,2] 
result = findKthRotation(arr)
print(result)