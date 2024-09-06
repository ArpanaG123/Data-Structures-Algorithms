# Single Number II

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

# TC = 0(N)
# SC = 0(N)


nums  = [2,2,3,2]

res = 0

for i in range(32):
    sm = 0

    for num in nums:
        if (num >> i) & 1 == 1:
            sm += 1
        if sm % 3 != 0:
            res = res | 1 << i
print(res)

# TC = 0(N)
# SC = 0(1)
