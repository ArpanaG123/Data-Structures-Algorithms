# Bitwise AND of Numbers Range
# Link - https://leetcode.com/problems/bitwise-and-of-numbers-range/description/

left = 5
right = 7
# Output: 4

# Approach1
l = 5
r = 7
ans = l

for i in range(l,r+1):
    ans = ans & i
print(ans)

# Approach2
l = 5
r = 7

while l<r:
    r = r & r-1
print(r)

# Approach3
l = 5
r = 7
cnt = 0
while l != r:
    l = l>>1
    r = r>>1
    cnt += 1
print(l<<cnt)