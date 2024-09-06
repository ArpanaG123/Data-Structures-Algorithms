# Single Number III
# Link - https://leetcode.com/problems/single-number-iii/description/

nums = [1,2,1,3,2,5] 
# output = [3,5]

# Method 1 - using bitwise
nums = [1,2,1,3,2,5]
n = len(nums)

xor_all = 0

for i in range(0,n):
    xor_all = xor_all ^ nums[i]

LSB = xor_all & ~(xor_all - 1)

bucket1 = []
bucket2 = []

for num in nums:
    if num & LSB == 0:
        bucket1.append(num)
    else:
        bucket2.append(num)

ans1 = 0
ans2 = 0
for b1 in bucket1:
    ans1 = ans1 ^ b1

for b2 in bucket2:
    ans2 = ans2 ^ b2

print([ans1,ans2])

# TC = 0(N)
# SC = 0(1)