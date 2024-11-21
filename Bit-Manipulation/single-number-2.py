# Single Number II
# Link - https://leetcode.com/problems/single-number-ii/description/

nums = [2,2,3,2]
# Output: 3
# Explanation: 3 is present only once.

freq = {}

for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
        
for k,v in freq.items():
    if v == 1:
        print(k)
# print(-1)

# TC = 0(N*log m) + 0(m)
# SC = 0(m),where m is the size of hashmap as logrithmic bcoz we are taking unordered map.


nums  = [2,2,3,2]
n = len(nums)
res = 0

for bit in range(32):
    cnt = 0
    
    for i in range(0,n):
        if nums[i] & (1<<bit):
            cnt += 1
    if cnt % 3 == 1:
        res = res | 1<<bit

if res >= 2**31:
    res -= 2**32

print(res)

# TC = 0(N*32)
# SC = 0(1)
