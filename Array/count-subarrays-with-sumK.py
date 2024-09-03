# Count subarrays with given sum. - Done
# Link - https://leetcode.com/problems/subarray-sum-equals-k/description/

nums = [1,2,3]
k = 3
# Output: 2

# Method1 - Brute force

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

# Method2 - Optimal
nums = [1,2,3]
k = 3
n = len(nums)

count = 0
sm = 0

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
