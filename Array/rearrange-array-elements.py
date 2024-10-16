# Rearrange Array Elements by Sign
# Link - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

# You should return the array of nums such that the the array follows the given conditions:
# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.


nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]

# Brute force
arr = [3,1,-2,-5,2,-4]

n = len(arr)
pos_el = []
neg_el = []

for i in range(0,n):
    if arr[i] > 0:
        pos_el.append(arr[i])
    else:
        neg_el.append(arr[i])
                
for i in range(0,n//2):
    arr[2*i] = pos_el[i]
    arr[2*i+1] = neg_el[i]
print(arr)

# TC = 0(N) + 0(N)
# SC = 0(N/2) + 0(N/2) = 0(N)

# Optimal approach
arr = [3,1,-2,-5,2,-4]

n = len(arr)

ans = [0]*n
posIdx = 0
negIdx = 1

for i in range(0,n):
    if arr[i] < 0:
        ans[negIdx] = arr[i]
        negIdx += 2
    else:
        ans[posIdx] = arr[i]
        posIdx += 2
print(ans)

# TC = 0(N)
# SC = 0(N)

# Varitey 2
arr = [-1,2,3,4,-3,1]
arr = [2,1,4,-7,-1,-3,3,-5,-8,-6]
n = len(arr)

posIdx = []
negIdx = []

for i in range(0,n):
    if arr[i] < 0:
        negIdx.append(arr[i])
    else:
        posIdx.append(arr[i])
        
l = len(posIdx)
m = len(negIdx)

if l > m:
    for i in range(0,m):
        arr[2*i] = posIdx[i]
        arr[2*i+1] = negIdx[i]
        
    idx = m*2
    for i in range(m,l):
        arr[idx] = posIdx[i]
        idx += 1
else:
    for i in range(0,l):
        arr[2*i] = posIdx[i]
        arr[2*i+1] = negIdx[i]
    idx = l*2
    for i in range(l,m):
        arr[idx] = negIdx[i]
        idx += 1
print(arr)

# output = if neg > pos = [2, -7, 1, -1, 4, -3, 3, -5, -8, -6]
# Output = if pos > neg = [2, -1, 3, -3, 4, 1]