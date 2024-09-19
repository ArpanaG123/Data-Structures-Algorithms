# find Largest sum contiguous Subarray. [V. IMP],kadanes's algorithm
# Link - https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0
# Link2 - https://leetcode.com/problems/maximum-subarray/description/

arr = [1, 2, 3, -2, 5]
# Output: 9
# Explanation: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.

# Method1 - Brute force
arr = [-2,1,-3,4,-1,2,1,-5,4]

n = len(arr)

mx = float('-inf')
start = -1
end = -1
for i in range(0,n):
    for j in range(i,n):
        sm = 0
        for k in range(i,j+1):
            sm += arr[k]
            
            if sm > mx:
                mx = sm
                start = i
                end = j
        
print(f"subarray with maximum sum is: {mx}")
print(f"elements with maximum sum is from index:{start} to {end}")
print(f"subarray elements with maximum sum: {arr[start:end+1]}")

# Output
# subarray with maximum sum is: 6
# elements with maximum sum is from index:3 to 6
# subarray elements with maximum sum: [4, -1, 2, 1]

# Time Complexity: O(n^3)
# Space Complexity: O(1)

# Method2 - Better Approach
arr = [-2,1,-3,4,-1,2,1,-5,4]

n = len(arr)

mx = float('-inf')
start = -1
end = -1
for i in range(0,n):
    sm = 0
    for j in range(i,n):
        sm += arr[j]
            
        if sm > mx:
            mx = sm
            start = i
            end = j
        
print(f"subarray with maximum sum is: {mx}")
print(f"elements with maximum sum is from index:{start} to {end}")
print(f"subarray elements with maximum sum: {arr[start:end+1]}")

# Output
# subarray with maximum sum is: 6
# elements with maximum sum is from index:3 to 6
# subarray elements with maximum sum: [4, -1, 2, 1]

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

arr = [-2,1,-3,4,-1,2,1,-5,4]

n = len(arr)
mx = float('-inf')

start = -1
end = -1

temp_start = 0

sm = 0
for i in range(0,n):
    sm += arr[i]
    
    if sm == 0:
        temp_start = i
    
    if sm > mx:
        mx = sm
        start = temp_start
        end = i
    
    if sm < 0:
        sm = 0
        temp_start = i+1
        
print(f"subarray with maximum sum is: {mx}")
print(f"elements with maximum sum is from index:{start} to {end}")
print(f"subarray elements with maximum sum: {arr[start:end+1]}")

# TC = 0(N)
# sc = 0(1)
    




