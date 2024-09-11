# Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Link - https://leetcode.com/problems/move-zeroes/description/

nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Brute force

nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

n = len(nums)

temp = []

for i in range(0,n):
    if nums[i] != 0:
        temp.append(nums[i])

nz = len(temp)

for i in range(0,nz):
    nums[i] = temp[i]

for i in range(nz,n):
    nums[i] = 0
print(nums)

# TC = 0(n) + 0(sizeofnonZero) + 0(n - sizeofnonZero) = 0(2n)
# sc = 0(size of non zero) = 0(n)

# Method2 - Optimal solution - using two pointer


nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

n = len(nums)

j = -1
for i in range(0,n):
    if nums[i] == 0:
        j = i
        break

if j == -1:
    print(nums)

for i in range(j+1,n):
    if nums[i] != 0:
        nums[i],nums[j] = nums[j],nums[i]
        j += 1
print(nums)

# TC = 0(N)
# SC = 0(1)

