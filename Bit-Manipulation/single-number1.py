# Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Link - https://leetcode.com/problems/single-number/description/

# Method1 - Brute force

nums = [1,2,1,2,4]

n = len(nums)

for i in range(0,n):
    count = 0
    for j in range(n):
        if nums[i] == nums[j]:
            count += 1
    if count == 1:
        print(nums[i])
        break

# TC = 0(N^2)
# SC = 0(1)

# Method2 - using sorting

nums = [4,2,1,2,1]
n = len(nums)

nums.sort()

for i in range(0,n-1,2):
    if nums[i] != nums[i+1]:
        print(nums[i])

# If no element found in loop, the last element is the single one
print(nums[-1])

# TC = 0(N logN)
# SC = 0(1)

# Method3 - Hashmap

nums = [1,2,1,2,4]

n = len(nums)
freq = {}
 
for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
# print(freq)

for k,v in freq.items():
    if v == 1:
        print(k)

# TC = 0(N)
# SC = 0(N)

# Method4 - XOR method(Bits manipulation)
nums = [1,2,1,2,4]
n = len(nums)

xor = 0
for i in range(0,n):
    xor ^= nums[i]
print(xor)

# TC = 0(N)
# SC = 0(1)

