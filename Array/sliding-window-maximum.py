# Sliding Window Maximum
# Link - https://leetcode.com/problems/sliding-window-maximum/description/

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

 

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]

# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Approach1 - Brute force

def maxSlidingWindow(nums,k):
    n = len(nums)
    
    ans = []
     
    for i in range(n-k+1):
        window = nums[i:i+k]
    
        ans.append(max(window))
      
    return ans
    
nums = [1,3,-1,-3,5,3,6,7]
k = 3 

res = maxSlidingWindow(nums,k)
print(res)

# Approach2 - using deque

from collections import deque

class MaxSlidingWindow:
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k
        
    def solve(self):
        nums = self.arr
        k = self.k

        n = len(nums)
        ans = []

        deq = deque()

        for i in range(n):
            # Remove indices that are out of the current window
            if deq and deq[0] < i-k+1:
                deq.popleft()

            # Remove indices whose corresponding values are less than nums[i]
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            # Add current index to the deque
            deq.append(i)

            # Append the maximum value of the current window to the result list
            if i >= k - 1:
                ans.append(nums[deq[0]])

        return ans
