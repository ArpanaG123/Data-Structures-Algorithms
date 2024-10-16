# Majority Element II
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Link - https://leetcode.com/problems/majority-element-ii/description/

# Brue force
arr = [1,1,1,3,3,2,2,2]

n = len(arr)

ans = set()

for i in range(0,n):
    cnt = 0
    for j in range(0,n):
        if arr[i] == arr[j]:
            cnt += 1
    if cnt > n//3:
        ans.add(arr[i])
print(list(ans))

# TC = 0(N^2)
# SC = 0(N)

# using hashing
arr = [1, 1, 1, 3, 3, 2, 2, 2]
n = len(arr)

# Dictionary to store frequency counts
freq = {}

# Count the frequency of each element
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Store elements that appear more than n // 3 times
ans = set()
for key, value in freq.items():
    if value > n // 3:
        ans.add(key)

# Convert set to list and print result
print(list(ans))

# TC = 0(N)
# SC = 0(N)

# using moore's agorithm

nums = [1,1,1,3,3,2,2,2]
# output = [1,2]

def majorityElement(nums):
    n = len(nums)
    
    cnt1 = 0
    cnt2 = 0
    
    el1 = float('-inf')
    el2 = float('-inf')
    
    for i in range(n):
        if cnt1 == 0 and nums[i] != el2:
            cnt1 = 1
            el1 = nums[i]
        elif cnt2 == 0 and nums[i] != el1:
            cnt2 = 1
            el2 = nums[i]
        elif nums[i] == el1:
            cnt1 += 1
        elif nums[i] == el2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1
            
    count1 = 0
    count2 = 0
    
    for i in range(n):
        if nums[i] == el1:
            count1 += 1
        elif nums[i] == el2:
            count2 += 1
    
    res = []
    if count1 > n//3:
        res.append(el1)
    if count2 > n//3:
        res.append(el2)
        
    return res

result = majorityElement(nums)
print(result)
