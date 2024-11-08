# Count subarrays with given sum. - Done
# Link - https://leetcode.com/problems/subarray-sum-equals-k/description/

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

nums = [1,2,3]
k = 3
# Output: 2

# Method1 - Brute force

arr = [1,1,1]
S = 2

n = len(arr)
cnt = 0

for i in range(0,n):
    for j in range(i,n):
        sm = 0
        for k in range(i,j+1):
            sm += arr[k]
        
        if sm == S:
            cnt += 1
print(cnt)

# TC = 0(N^3)
# sc = 0(1)

# Better approach

nums = [1,2,3]
k = 3
n = len(nums)

count = 0

for i in range(0,n):
    sm = 0
    for j in range(i,n):
        sm += nums[j]

        if sm == k:
            count += 1
print(count)

# TC = 0(N^2)
# sc = 0(1)

# Method3 - Optimal
nums = [1,2,3]
k = 3
n = len(nums)

count = 0
sm = 0

# This ensures that if the cumulative sum sm equals to k at any point, a valid subarray is found right from the beginning.
freq = {0:1}

for i in range(0,n):
    sm += nums[i]
            
    rem = sm - k

    if rem in freq:
        count += freq[rem]
            
    if sm in freq:
        freq[sm]+= 1
    else:
        freq[sm] = 1
        
print(count)
