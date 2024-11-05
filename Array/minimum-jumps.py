# Minimum Jumps
# Link - https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1
# link - https://leetcode.com/problems/jump-game/description/

# Given an array arr[] of non-negative integers. Each array element represents the maximum length of the jumps that can be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x. Find the minimum number of jumps to reach the end of the array starting from the first element. If an element is 0, then you cannot move through that element.
# Note:  Return -1 if you can't reach the end of the array.

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# Output: 3 
# Output = true
# Explanation: First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last

nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

def minJumps(arr):
    n = len(arr)
    
    maxIndx = 0
    for i in range(0,n):
        if i > maxIndx:
            return False
        maxIndx = max(maxIndx,i + arr[i])
    return True

arr = [2,3,1,1,4]
result = minJumps(arr)
print(result)


# Link - https://leetcode.com/problems/jump-game-ii/

def minJumps(arr):
    n = len(arr)
    
    if n == 1:
        return 0  # If there's only one element, no jump is needed
    
    jumps = 0          # Number of jumps required
    maxReach = 0       # Farthest we can reach
    endOfCurrentJump = 0  # End of the current jump range
    
    for i in range(n - 1):  # We stop at n-1 because we don't need to jump from the last element
        maxReach = max(maxReach, i + arr[i])  # Update the farthest we can reach
        
        # If we reach the end of the current jump range, we need to jump
        if i == endOfCurrentJump:
            jumps += 1
            endOfCurrentJump = maxReach  # Update the range for the next jump
            
            # If the farthest point we can reach is beyond or at the last index, return the jump count
            if endOfCurrentJump >= n - 1:
                return jumps
    
    return -1  # If we can't reach the end, return -1

# Test case
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
result = minJumps(arr)
print(result)