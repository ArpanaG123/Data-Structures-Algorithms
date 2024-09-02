# find Largest sum contiguous Subarray. [V. IMP]
# Link - https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0
# Link2 - https://leetcode.com/problems/maximum-subarray/description/

arr = [1, 2, 3, -2, 5]
# Output: 9
# Explanation: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.

# Method1 - Brute force
arr = [1, 2, 3, -2, 5]
n = len(arr)

res = []

for i in range(0,n):
    for j in range(i,n):
        subarrays = arr[i:j+1]
        sm = sum(subarrays)
        res.append(sm)
print(max(res))

# Time Complexity: O(n^3)
# Space Complexity: O(n^2)

# Method2 - Improved brute force
arr = [1, 2, 3, -2, 5]
n = len(arr)

max_sum = float("-inf")

for i in range(0,n):
    curr_sum = 0
    for j in range(i,n):
        curr_sum += arr[j]
        max_sum = max(curr_sum,max_sum)
print(max_sum)

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Method3 - Kadane's Algorithm
# Kadane’s Algorithm:
# Explanation: This is the most efficient approach to solve the problem.
# Time Complexity: O(n)
# Space Complexity: O(1)

# statement:
# The algorithm maintains a running sum and tracks the maximum sum encountered so far.
# If the running sum becomes negative, it resets to 0, as continuing with a negative sum would only decrease the total sum.

arr = [-2,-3,4,-1,-2,1,5,-3]

n = len(arr)

maxi = float('-inf')
sm = 0
resStart = -1
resEnd = -1

start = 0

for i in range(0,n):

    sm += arr[i]

    if sm == 0:
        start = i
    
    if sm > maxi:
        maxi = sm
        resStart = start
        resEnd = i
    
    if sm < 0:
        sm = 0
        start = i+1

print("Largest contigous subarray is :",sm)
print("start index: ",resStart)
print("End index: ",resEnd)

# TC = 0(N)
# sc = 0(1)
    




