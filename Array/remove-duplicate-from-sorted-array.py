# Remove Duplicates from Sorted Array
# Link - https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Approach1 - using set

print("Try programiz.pro")

nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 2, nums = [1,2,_]

res = set()

for i in nums:
    res.add(i)
    
idx = 0
for num in res:
    nums[idx] = num
    idx += 1
    
print(idx)
# TC = 0(N + NlogN)
# SC = 0(N)
# As to insert into set time complexity is NlogN

# Approach2 - using two pointer

nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 2, nums = [1,2,_]

n = len(nums)
i = 0
for j in range(1,n):
    if nums[j] != nums[i]:
        nums[i+1] = nums[j]
        i += 1
print(i+1)

# TC = 0(N)
# SC = 0(1)
