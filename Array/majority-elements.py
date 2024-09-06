# Majority elements
# Link - https://leetcode.com/problems/majority-element/description/

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

nums = [3,2,3]
# Output: 3

# Brute force
nums = [3, 2, 2]
n = len(nums)

res = []

# Brute force method to count the elements
for i in range(n):
    cnt = 0
    for j in range(n):
        if nums[i] == nums[j]:
            cnt += 1
    
    # If count is >= n // 2 and element not already in the result
    if cnt >= n // 2 and nums[i] not in res:
        res.append(nums[i])

print("Elements with count >= n//2:", res)
print("Total number of such elements:", len(res))

# Method2 - using moore's voting algotithm
nums = [1,2,2]

n = len(nums)

candidate = nums[0]
cnt = 0

for i in range(n):
    if cnt == 0:
        candidate = nums[i]
    if nums[i] == candidate:
        cnt += 1
    else:
        cnt -= 1

print("Candidates count with greater than n//2:",candidate)
