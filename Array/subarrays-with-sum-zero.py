# Subarrays with sum is 0
# Find if there is any subarray with sum equal to 0.
# Link - https://www.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1

arr = [4,2,-3,1,6]
# Output: Yes
# Explanation: 2, -3, 1 is the subarray with sum 0.

# Method1 - Brute force
# Check all possible subarrays and compute their sum. If the sum is zero, print the subarray.

arr = [4,2,-3,1,6]
n = len(arr)

for i in range(0,n):
    for j in range(i,n):
        sm = 0
        for k in range(i,j+1):
            sm += arr[k]

        if sm == 0:
            print("Yes")
            print(f"Subarray with zero sum from index {i} to {j}: {arr[i:j+1]}")

# TC = 0(N^3)
# SC = 0(1)


# Method2 - Improved brute force
# Description: Instead of recalculating the sum for each subarray, maintain a running sum and check if it equals zero.
arr = [4,2,-3,1,6]
n = len(arr)

for i in range(0,n):
    sm = 0
    for j in range(i,n):
        sm += arr[j]

        if sm == 0:
            print("Yes")
            print(f"Subarray with zero sum from index {i} to {j}: {arr[i:j+1]}")

# TC = 0(N^2)
# SC = 0(1)

# Method3 - Optimal and efficient - hashmap

arr = [4,2,-3,1,6]
n = len(arr)

freq = {}
sm = 0

for i in range(0,n):
    sm += arr[i]
    
    if sm == 0:
        print("yes")
        print(f"Subarray with zero sum found from index 0 to {i}: {arr[0:i+1]}")
    
    if sm in freq:
        prev_idx = freq[sm]
        print("Yes")
        print(f"Subarray with zero sum found from index {prev_idx + 1} to {i}: {arr[prev_idx + 1:i+1]}")
    else:
        freq[sm] = i
# print(freq)

# TC = 0(N)
# SC = 0(N)
